# Horn nii-san's **Improved** RenPy Person class
## Minimalist, cleaner, easier!


## Improved Person Class
**Defined in `person.rpy`**
This is a smarter, cleaner way to define characters in Ren'Py.


### Old way (booooring)
```py
$ horn = Character("Horn nii-san", color="#fff", what_font="Serif", who_font="Serif", who_outlines=[(1.0, "#000")])
```

### New way
```py
$ horn = Person("Horn nii-san", color="#fff", what_font="Serif", who_font="Serif")
```

###Example usage in `script.py`
```py
horn "Hello there!"
horn.s "This is also valid."
```
Both lines above work thanks to `__call__()` and `__getattr__()` handling.



## Improved Points Class
### See `points.rpy` for the Points class.
⚠️ You need `person.rpy` for this to work.
(Be sure to remove the \# before `self.pts = points if points else Points()` in `person.rpy`)

### Example Setup
```py
$ horn = Person("Horn nii-san", color="#fff", points=Points())
```

### Old way
```py
$ horn_lovepoints += 1
$ horn_angrypoints += 1
horn "You're hurting my feelings."
```

### New way
```py
$ horn.pts.love += 1
$ horn.pts.anger += 1
horn("You're hurting my [horn.pts.love] feelings.")
```
Which is slightly better!


### Example usage in `script.py`
```py
label start:
    horn "Hey [mc.name]"
    mc "Hey Horn, you're looking rather handsome today."

    $ horn.pts.love += 1
    horn "That's really sweet."

    mc "Just kidding, you're ugly."
    $ horn.pts.anger += 1
    horn "Rude."
```

That’s it! Now your Ren'Py code looks like it was written in 2025, not 2005.
Simple. Elegant. Horn-approved™
