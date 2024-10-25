### Coding Challenges

> I tried displaying the allergies within the admin console and received an MSFList error. Feedback: The error you're seeing is because MultiSelectField returns a list-like object (MSFList) which doesn't have an .all() method. 
Instead, you should iterate directly over the allergies attribute without calling .all().


<details>

<summary>Project Changes</summary>

> 10/25/24

- [x] Sample Recipes added at admin console
- [x] Search functionality. User can search by title or ingredient.
- [x] Users can add a recipe from their profile. Some logic built into view to break steps and ingredients into separate line based on '\n' characters

> 10/24/24

- [x] Additional profile fields can be updated. First and Last name
- [x] Users can add profile images

> 10/22/24

- [x] Moved User creation and allergy customization to this testenv

</details>

### Major Features

- [x] User Profile
- [x] User Profile (custom detials)
- [x] Search recipes in .db
- [x] User can add recipes to .db
 