# tagproject
Develop a text saving and retrieval web app using Django. The app should be able to save short text snippets with a title, timestamp and created user. The snippet should also contain a relation to a Tag model (simple model with only title field). Tag title should be unique. Do not create tags for every snippet, check whether the tag with the same title exists or not before creating a new one. If the same tag exists link to that tag. Implement JWT authentication for getting user.

Expected output format: Github repository url.

Authentication API:
1. Login API
2. Refresh API
CRUD APIs:
1. Overview API (total count, listing)
Total number of snippet and  List all available snippets with a hyperlink to respective detail APIs.
2. Create API
API to collect the snippet information and save the data to DB.
3. Detail API
API should display the snippet title, content, and timestamp information.
4. Update API
API to update individual items. Update API should return item detail response.

5. Delete API
API  to delete selected items and return the list of items as response.
6. Tag list API
API to list tags
7. Tag Detail API
API to return snippets linked to the selected tag.
