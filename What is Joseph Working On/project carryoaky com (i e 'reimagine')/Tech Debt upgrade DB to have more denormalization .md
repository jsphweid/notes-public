# Tech Debt: upgrade DB to have more denormalization and default sort orders that make sense

Priority: Priority Medium
Size: Size Long
Status: Not started

- [ ]  segments sort key should probably have offset at the front so we don't have to order them through the application
- [ ]  recordings should have pieceId, arrangementId denormalized in the db object to avoid excessive round trips
- [ ]  pieces should display in alphabetical order by default

use this process of thinking and extend it to all database entity types