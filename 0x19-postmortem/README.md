# PostMortem StreamRunners

## Issue Summary

Issue started the 28 September at 2pm (Paris) and ended at 3:40pm (Paris) of the same day.

The issue impacted 100% of user and disabled the ability to participate to raffle and to see previous raffle or previous raffle participation.

### Root Cause :

When we're trying to import 600 raffles manually in the database, we forgot to add the region condition, so to undo that we've planned to DROP all the new raffle added, a conditions was missing on the SQL Line, who result on the deleting off every raffle.

## Timeline

Issue started the 28 September at 2pm (Paris) and ended at 5pm (Paris) of the same day.

We detect the issue by using one of our monitoring system made by ourself called "Automated report" (see exemple below, note that is exemple is not the same report as this PostMortem) :

![img](http://image.noelshack.com/fichiers/2022/39/4/1664445954-screenshot-61.png)

### Action Taken

1. What we do firt is to download the last backup of the database (we do backup everynight).
2. While backup is downloading we inform all user with a notification of the problem on raffle page.
3. We import the backup of the raffle table on the database.
4. Next step was the most complicate, because we have a backup of the day before, but people participate to raffle the day of the incident, so we have to link participation to the raffle.


### Escalate

The incident scale to the communication and moderation teams, because they have to say about the incident for people who asking.

## Corrective and preventing

To prevent the issue, we have a safety mode in MySQL Workbench, the developper desactived it because it was easier to work with out, but with it nothing about that happen.

