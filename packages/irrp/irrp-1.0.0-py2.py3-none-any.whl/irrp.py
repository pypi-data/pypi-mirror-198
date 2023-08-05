"""
Basically [irrp.py](https://abyz.me.uk/rpi/pigpio/code/irrp_py.zip) but
as a python module"""

__version__ = "1.0.0"

import time


import pigpio


class ShortCodeError(Exception):
    pass


# https://abyz.me.uk/rpi/pigpio/examples.html
# based on https://abyz.me.uk/rpi/pigpio/code/irrp_py.zip
class RecordReplayer:
    def __init__(
        self,
        pi,
        freq=38.0,  # frequency kHz (--freq)
        gap=100,  # key gap ms (--gap)
        glitch=100,  # glitch us (--glitch)
        post=15,  # postamble ms (--post)
        pre=200,  # preamble ms (--pre)
        short=10,  # short code length (--short)
        tolerance=15,  # tolerance percent (--tolerance)
    ):
        self.pi = pi
        self.GLITCH = glitch
        self.PRE_MS = pre
        self.POST_MS = post
        self.FREQ = freq
        self.SHORT = short
        self.GAP_MS = gap
        self.TOLERANCE = tolerance

        self.TOLER_MIN = (100 - self.TOLERANCE) / 100.0
        self.TOLER_MAX = (100 + self.TOLERANCE) / 100.0

        self.POST_US = self.POST_MS * 1000
        self.PRE_US = self.PRE_MS * 1000
        self.GAP_S = self.GAP_MS / 1000.0

    last_tick = 0
    in_code = False
    code = []
    fetching_code = False

    def _carrier(self, gpio, frequency, micros):
        """
        Generate carrier square wave.
        """
        wf = []
        cycle = 1000.0 / frequency
        cycles = int(round(micros / cycle))
        on = int(round(cycle / 2.0))
        sofar = 0
        for c in range(cycles):
            target = int(round((c + 1) * cycle))
            sofar += on
            off = target - sofar
            sofar += off
            wf.append(pigpio.pulse(1 << gpio, 0, on))
            wf.append(pigpio.pulse(0, 1 << gpio, off))
        return wf

    def _normalise(self, c):
        """
        Typically a code will be made up of two or three distinct
        marks (carrier) and spaces (no carrier) of different lengths.

        Because of transmission and reception errors those pulses
        which should all be x micros long will have a variance around x.

        This function identifies the distinct pulses and takes the
        average of the lengths making up each distinct pulse.  Marks
        and spaces are processed separately.

        This makes the eventual generation of waves much more efficient.

        Input

        M    S   M   S   M   S   M    S   M    S   M
        9000 4500 600 540 620 560 590 1660 620 1690 615

        Distinct marks

        9000                average 9000
        600 620 590 620 615 average  609

        Distinct spaces

        4500                average 4500
        540 560             average  550
        1660 1690           average 1675

        Output

        M    S   M   S   M   S   M    S   M    S   M
        9000 4500 609 550 609 550 609 1675 609 1675 609
        """
        entries = len(c)
        p = [0] * entries  # Set all entries not processed.
        for i in range(entries):
            if not p[i]:  # Not processed?
                v = c[i]
                tot = v
                similar = 1.0

                # Find all pulses with similar lengths to the start pulse.
                for j in range(i + 2, entries, 2):
                    if not p[j]:  # Unprocessed.
                        if (
                            (c[j] * self.TOLER_MIN) < v < (c[j] * self.TOLER_MAX)
                        ):  # Similar.
                            tot = tot + c[j]
                            similar += 1.0

                # Calculate the average pulse length.
                newv = round(tot / similar, 2)
                c[i] = newv

                # Set all similar pulses to the average value.
                for j in range(i + 2, entries, 2):
                    if not p[j]:  # Unprocessed.
                        if (
                            (c[j] * self.TOLER_MIN) < v < (c[j] * self.TOLER_MAX)
                        ):  # Similar.
                            c[j] = newv
                            p[j] = 1

    def _tidy_mark_space(self, rec, base):
        ms = {}

        # Find all the unique marks (base=0) or spaces (base=1)
        # and count the number of times they appear,

        rl = len(rec)
        for i in range(base, rl, 2):
            if rec[i] in ms:
                ms[rec[i]] += 1
            else:
                ms[rec[i]] = 1

        v = None

        for plen in sorted(ms):
            # Now go through in order, shortest first, and collapse
            # pulses which are the same within a tolerance to the
            # same value.  The value is the weighted average of the
            # occurences.
            #
            # E.g. 500x20 550x30 600x30  1000x10 1100x10  1700x5 1750x5
            #
            # becomes 556(x80) 1050(x20) 1725(x10)
            #
            if v == None:
                e = [plen]
                v = plen
                tot = plen * ms[plen]
                similar = ms[plen]

            elif plen < (v * self.TOLER_MAX):
                e.append(plen)
                tot += plen * ms[plen]
                similar += ms[plen]

            else:
                v = int(round(tot / float(similar)))
                # set all previous to v
                for i in e:
                    ms[i] = v
                e = [plen]
                v = plen
                tot = plen * ms[plen]
                similar = ms[plen]

        v = int(round(tot / float(similar)))
        # set all previous to v
        for i in e:
            ms[i] = v

        rl = len(rec)
        for i in range(base, rl, 2):
            rec[i] = ms[rec[i]]

    def _tidy(self, records):
        self._tidy_mark_space(records, 0)  # Marks.
        self._tidy_mark_space(records, 1)  # Spaces.

    def _end_of_code(self):
        if len(self.code) > self.SHORT:
            self._normalise(self.code)
            self.fetching_code = False
        else:
            self.code = []
            raise ShortCodeError()

    def _cbf(self, gpio, level, tick):
        if level != pigpio.TIMEOUT:
            edge = pigpio.tickDiff(self.last_tick, tick)
            self.last_tick = tick

            if self.fetching_code:
                if (edge > self.PRE_US) and (not self.in_code):  # Start of a code.
                    self.in_code = True
                    self.pi.set_watchdog(gpio, self.POST_MS)  # Start watchdog.

                elif (edge > self.POST_US) and self.in_code:  # End of a code.
                    self.in_code = False
                    self.pi.set_watchdog(gpio, 0)  # Cancel watchdog.
                    self._end_of_code()

                elif self.in_code:
                    self.code.append(edge)

        else:
            self.pi.set_watchdog(gpio, 0)  # Cancel watchdog.
            if self.in_code:
                self.in_code = False
                self._end_of_code()

    def record(self, gpio):
        self.pi.set_mode(gpio, pigpio.INPUT)  # IR RX connected to this GPIO.
        self.pi.set_glitch_filter(gpio, self.GLITCH)  # Ignore glitches.

        cb = self.pi.callback(gpio, pigpio.EITHER_EDGE, self._cbf)
        self.code = []
        self.fetching_code = True
        while self.fetching_code:
            time.sleep(0.1)

        time.sleep(0.5)
        self.pi.set_glitch_filter(gpio, 0)  # Cancel glitch filter.
        self.pi.set_watchdog(gpio, 0)  # Cancel watchdog.

        records = self.code[:]
        self._tidy(records)
        cb.cancel()
        return records

    def replay(self, gpio, code):
        self.pi.set_mode(gpio, pigpio.OUTPUT)  # IR TX connected to this GPIO.
        self.pi.wave_add_new()

        emit_time = time.time()

        # Create wave
        marks_wid = {}
        spaces_wid = {}

        wave = [0] * len(code)
        for i in range(0, len(code)):
            ci = code[i]
            if i & 1:  # Space
                if ci not in spaces_wid:
                    self.pi.wave_add_generic([pigpio.pulse(0, 0, ci)])
                    spaces_wid[ci] = self.pi.wave_create()
                wave[i] = spaces_wid[ci]
            else:  # Mark
                if ci not in marks_wid:
                    wf = self._carrier(gpio, self.FREQ, ci)
                    self.pi.wave_add_generic(wf)
                    marks_wid[ci] = self.pi.wave_create()
                wave[i] = marks_wid[ci]

        delay = emit_time - time.time()

        if delay > 0.0:
            time.sleep(delay)

        self.pi.wave_chain(wave)

        while self.pi.wave_tx_busy():
            time.sleep(0.002)

        emit_time = time.time() + self.GAP_S

        for i in marks_wid:
            self.pi.wave_delete(marks_wid[i])

        for i in spaces_wid:
            self.pi.wave_delete(spaces_wid[i])

    def compare(self, p1, p2):
        """
        Check that both recodings correspond in pulse length to within
        TOLERANCE%.  If they do average the two recordings pulse lengths.

        Input

            M    S   M   S   M   S   M    S   M    S   M
        1: 9000 4500 600 560 600 560 600 1700 600 1700 600
        2: 9020 4570 590 550 590 550 590 1640 590 1640 590

        Output

        A: 9010 4535 595 555 595 555 595 1670 595 1670 595
        """
        if len(p1) != len(p2):
            return False

        for i in range(len(p1)):
            v = p1[i] / p2[i]
            if (v < self.TOLER_MIN) or (v > self.TOLER_MAX):
                return False

        for i in range(len(p1)):
            p1[i] = int(round((p1[i] + p2[i]) / 2.0))

        return True
