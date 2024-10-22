### Coding Challenges

> I tried displaying the allergies within the admin console and received an MSFList error. Feedback: The error you're seeing is because MultiSelectField returns a list-like object (MSFList) which doesn't have an .all() method. 
Instead, you should iterate directly over the allergies attribute without calling .all().
