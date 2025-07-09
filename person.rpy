init python:
    class Person():
        def __init__(
            self,
            name,
            color="#fff",
            what_color="#fff",
            who_outlines=[ (1.0, "#000") ],
            what_outlines=[ (0.8, "#000") ],
            who_font=None,
            what_font=None,
            who_size=30,
            what_size=30,
            points=None
        ):
            self.name = name
            self.s = Character(
                name,
                color=color,
                what_color=what_color,
                who_font=who_font,
                what_font=what_font,
                who_outlines=who_outlines,
                what_outlines=what_outlines,
                who_size=who_size,
                what_size=what_size
            )
            # self.pts = points if points else Points() # Uncomment this for the Points() class to work

        def __getattr__(self, attr):
            if attr == "s":
                raise AttributeError
            return getattr(self.s, attr)

        def __call__(self, args, **kwargs):
            return self.s(args, **kwargs)
