# Change Log: Global Placeholders Implementation

**Date:** 2025-12-10
**Task:** Apply placeholders to all forms and remove labels.

## What I Did
I updated all the forms in the application to use **placeholders** inside the input fields instead of displaying separate labels above them. This change was applied to:
1.  **Signup Page**
2.  **Login Page** (and the logged-out homepage login section)
3.  **Create Post Page**
4.  **Edit Post Page**
5.  **Edit Profile Page**

## Why I Did It
The goal was to match the **Instagram-style design** requested by the user. Instagram and many modern applications use placeholders to create a cleaner, more minimalist interface. Removing the labels reduces visual clutter and makes the forms look more streamlined.

## How I Did It

### 1. Signup Page (`accounts/forms.py`)
*   **Modified `CustomUserCreationForm`**: I added a `widgets` dictionary to the `Meta` class.
*   **Action**: Assigned `forms.TextInput` (or `EmailInput`) widgets to the `email`, `name`, and `username` fields.
*   **Attributes**: Added `attrs={'placeholder': '...', 'class': 'form-control'}` to each widget to set the placeholder text and Bootstrap styling.

### 2. Login Page (`templates/registration/login.html` & `templates/home.html`)
*   **Manual Rendering**: Since the Login view uses Django's built-in `AuthenticationForm` (which is harder to customize without overriding the view), I manually rendered the HTML input fields in the templates.
*   **Action**: Replaced `{{ form.as_p }}` with `<input>` tags.
*   **Attributes**: Added `placeholder="Phone number, username or email address"` and `placeholder="Password"` directly to the HTML inputs.

### 3. Create/Edit Post (`todo/forms.py` & `todo/views.py`)
*   **Created `TodoForm`**: I created a new file `todo/forms.py` and defined a `TodoForm` class inheriting from `forms.ModelForm`.
*   **Widgets**: Defined widgets for `title` and `body` with appropriate placeholders.
*   **Updated Views**: In `todo/views.py`, I updated `StudyCreateView` and `StudyUpdateView` to use `form_class = TodoForm` instead of the auto-generated `fields` list.

### 4. Edit Profile (`accounts/forms.py` & `accounts/views.py`)
*   **Modified `CustomUserChangeForm`**: In `accounts/forms.py`, I added widgets for all profile fields (Profile Image, Bio, School, etc.).
*   **Attributes**: Added specific placeholders for each field (e.g., "Profile Image URL", "Bio", "School").
*   **Updated View**: In `accounts/views.py`, I updated `ProfileUpdateView` to use `form_class = CustomUserChangeForm`.
