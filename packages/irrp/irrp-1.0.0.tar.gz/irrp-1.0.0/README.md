# irrp

Basically [irrp.py](https://abyz.me.uk/rpi/pigpio/code/irrp_py.zip) but
as a python module so you can integrate it easily with your Python
program.

## Examples

### To record:
```py
import pigpio
pi = pigpio.pi()
gpio_pin = 18

# Record the IR data
import irrp
rr = irrp.RecordReplayer(pi)
print(rr.record(gpio_pin))

# optionally, save to a file:
import json
json.dump(open("data.json", "wb"))
```

### To replay:
```py
import pigpio
pi = pigpio.pi()
gpio_pin = 18

# load the recorded data
import json
data = json(load(open("data.json")))

# replay the data
import irrp
rr = irrp.RecordReplayer(pi)
rr.replay(gpio_pin, data)
```

### To record and compare data:
```py
import pigpio
pi = pigpio.pi()
gpio_pin = 18

# record data
import irrp
rr = irrp.RecordReplayer(pi)
rec = rr.record(gpio_pin)

import json
data = json(load(open("data.json")))
irrp.compare(data, rec)
```
