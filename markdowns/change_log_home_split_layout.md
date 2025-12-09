# Change Log: Home Page Split Layout & Theme Restoration

## Summary
Restored the "Instagram-style" 2-column layout for the logged-in home page and implemented a new split layout for the logged-out landing page. Also finalized global form styling and theme adjustments.

## Changes

### 1. Home Page (`templates/home.html`)
*   **Logged-In View:**
    *   Restored 2-column layout:
        *   **Left Column:** Feed of posts from followed users + self.
        *   **Right Column:** Sidebar with current User Profile and "Suggestions For You".
    *   Applied `glass-panel` and `card` styles consistent with the Glassmorphism theme (but on a gray background).
*   **Logged-Out View (Landing Page):**
    *   Implemented a **Split Layout**:
        *   **Left Side:** "Noesis" Branding and "Share Your Knowledge" subtext.
        *   **Right Side:** Embedded **Login Form** (manually rendered with placeholders) + "Sign Up" link box.
    *   Replaced the previous "Welcome Alert" or simple landing page logic.

### 2. Login Page (`templates/registration/login.html`)
*   **Overwritten with Manual Rendering:**
    *   Removed `{{ form.as_p }}`.
    *   Manually rendered `username` and `password` input fields.
    *   **Added Placeholders:** "Phone number, username or email address" and "Password".
    *   **Removed Labels:** Inputs have no corresponding `<label>` tags (or they are hidden via CSS).

### 3. Global CSS (`static/css/main.css`)
*   **Background Image:** Removed the vibrant background image.
*   **Background Color:** Restored standard light gray `#f8f9fa`.
*   **Navbar:** Removed `background: transparent !important` to allow the standard Bootstrap `bg-dark` to work.
*   **Glassmorphism:** Kept `.glass-panel` and modified `.card` styles to have transparency/blur effects.

### 4. Navbar (`templates/base.html`)
*   **Restored `bg-dark`:** Removed custom `glass-nav` class and reverted to `navbar-dark bg-dark` for a solid black navbar.

## Rationale
*   **User Preference:** The user specifically requested "their own theme" back but with specific adjustments (no background image, black navbar, split landing page with login form).
*   **Visual Consistency:** Manual rendering of forms ensures that the Login form on the home page matches the standalone Login page exactly (same placeholders, no labels).
