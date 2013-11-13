tweetSchedule
=============

Twitter Powered Scheduler built on top of Django and Celery

What?
=====

This is a simple system that takes tweets similar to:

```
#remindly #who friend1 friend2 #what Hangout and eat food #where McDonalds #when in 2 hours
```

It will then in two hours update the user's twitter status and put the following:

```
#who @friend1 @friend2 #what Hangout and eat food #where McDonalds
```

And, that is about it. To use the service the user needs to authorize the application with twitter,
once that has been done then they don't need to visit the site again to schedule things.
