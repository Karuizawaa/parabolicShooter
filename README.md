# parabolicShooter
This project focused on determine initial velocity to hit object with parabolic movement, and show the trajectory

to use this app, u need to install matplotlib, simply

pip install matplotlib --upgrade

to set elevation degree, set it on [this line](https://github.com/aldiroby/parabolicShooter/blob/a128adf94530e8e4c89e2f6edfe476252dd9f472/plot.py#L7)

`ANGLE = 45 #degree elevation`

this parameter will set the elevation degree to 45 degree.


to set the target, set it on [this line](https://github.com/aldiroby/parabolicShooter/blob/a128adf94530e8e4c89e2f6edfe476252dd9f472/plot.py#L32)

`plot(vshoot(4,3))`

this parameter will set the target on horizontal distance 4, and vertical distance +3 (taller than shooter), with meter units.
