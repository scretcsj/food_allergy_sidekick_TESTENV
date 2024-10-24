### Coding Challenges

> I tried displaying the allergies within the admin console and received an MSFList error. Feedback: The error you're seeing is because MultiSelectField returns a list-like object (MSFList) which doesn't have an .all() method. 
Instead, you should iterate directly over the allergies attribute without calling .all().


<details>

<summary>Project Changes</summary>

> 10/24/24

- [x] Additional profile fields can be updated. First and Last name
- [x] Users can add profile images

> 10/22/24

- [x] Moved User creation and allergy customization to this testenv

</details>
