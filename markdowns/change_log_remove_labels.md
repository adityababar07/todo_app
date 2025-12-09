# Change Log: Removing Labels from Forms

**Date:** 2025-12-10
**Task:** Remove labels from all forms to rely on placeholders.

## What I Did
I removed or hidden the field labels from the following pages:
1.  **Create Post Page** (`templates/todo_new.html`)
2.  **Edit Post Page** (`templates/todo_edit.html`)
3.  **Edit Profile Page** (`templates/profile_edit.html`)

## Why I Did It
Since I previously added **placeholders** to all these forms, the labels became redundant and cluttered the UI. Removing them aligns with the **Instagram-style** minimalist design requested.

## How I Did It

### 1. Create/Edit Post Pages
*   **File**: `templates/todo_new.html` and `templates/todo_edit.html`
*   **Action**: I manually removed the `<label>` HTML tag from the form loop.
*   **Code Change**:
    ```html
    <!-- Before -->
    <label class="form-label text-dark">{{ field.label }}</label>
    
    <!-- After -->
    <!-- Label removed for Instagram style -->
    ```

### 2. Edit Profile Page
*   **File**: `templates/profile_edit.html`
*   **Action**: Since this page uses `{{ form.as_p }}` which automatically renders labels, I added a CSS block to hide them.
*   **Code Change**:
    ```css
    form label {
        display: none;
    }
    ```
    I also added some basic styling to the inputs to make them look better without labels.
