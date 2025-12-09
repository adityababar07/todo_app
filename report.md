# Project Report: Student Knowledge Sharing Platform

## Changes and Improvements

### 1. UI/UX Overhaul
- **Glassmorphism Design**: Implemented a modern, visually appealing "Glassmorphism" design system using translucent backgrounds, blurs, and vibrant gradients.
- **Typography**: Integrated Google Fonts ('Inter') for a clean, modern look.
- **Branding**: Renamed the application from "To Do app" to "Noesis" to better reflect its purpose.
- **Responsive Layout**: Improved responsiveness for better mobile experience.

### 2. Functional Enhancements
- **Categories**: Added a `category` field to posts, allowing users to classify content as "Knowledge", "Idea", or "Question".
- **Knowledge Feed**: Transformed the simple list view into a rich "Knowledge Feed" with card-based layout, category badges, and improved readability.
- **Landing Page**: Created a welcoming landing page that clearly communicates the platform's value proposition.

### 3. Technical Updates
- **Database**: Switched to SQLite for easier local development and testing (as requested).
- **Dependencies**: Updated Django and other dependencies to newer, more secure versions compatible with Python 3.14.
- **Code Structure**: Refactored templates to use a consistent base template with the new design system.

### 4. Recent Bug Fixes & Refinements
- **UI Layout Fixes**:
    - **Navbar Overlap**: Added padding to the body to prevent content from being hidden behind the fixed navbar.
    - **Sticky Footer**: Implemented a flexbox layout to ensure the footer stays at the bottom of the page.
    - **Alert Visibility**: Moved alerts below the navbar and adjusted z-indices to ensure they are visible but do not cover dropdown menus.
- **Z-Index Correction**:
    - **Dropdown vs. Popup**: Fixed an issue where the alert popup covered the navbar dropdowns by explicitly setting the Navbar z-index (1050) higher than the Alert z-index (1020).
    - **HTML Structure**: Reordered elements in `base.html` to ensure logical stacking.
- **Logout Functionality**:
    - **HTTP 405 Error**: Fixed a "Method Not Allowed" error on logout by replacing the GET link with a POST form, complying with Django 5.0+ security standards.
- **Theme Reversion**:
    - **Minimal Design**: Reverted the UI from Glassmorphism back to a clean, minimal Bootstrap-based design as per user request, while retaining all functional improvements and layout fixes.
- **Profile Redesign**:
    - **Instagram Style**: Completely redesigned the profile page to mimic the Instagram layout (Header with stats/bio + 3-column post grid), while maintaining the minimal theme.
    - **Backend Logic**: Updated `ProfileView` to correctly fetch and display the specific user's posts and details.
- **Home Feed**:
    - **Instagram Layout**: Implemented a 2-column layout (Feed + Sidebar) for the home page.
    - **Follow System**: Added a `Follow` model and functionality, allowing users to follow others.
    - **Personalized Feed**: The home feed now displays posts only from followed users (and the user themselves), ordered by date.
    - **Suggestions**: Added a "Suggested for you" section in the sidebar.
    
### 5. Instagram-Style Redesign (Latest Updates)
- **Logged-Out Homepage**:
    - **Split Layout**: Implemented a split-screen design with the "Share Your Knowledge" content on the left and a login form on the right, mimicking the Instagram login page.
    - **Branding**: Prominently displayed the "Noesis" brand.
- **Signup Page**:
    - **Simplified Form**: Reduced fields to just Email, Full Name, Username, and Password.
    - **Visuals**: Centered card layout with "Noesis" branding and a "Log in with Facebook" button (visual only).
    - **Footer**: Added a "Have an account? Log in" section.
- **Login Page**:
    - **Consistent Design**: Matched the Signup page style with a centered card and "Noesis" branding.
    - **Placeholders**: Replaced field labels with placeholders ("Phone number, username or email address" and "Password") for a cleaner look.
    - **Footer**: Added a "Don't have an account? Sign up" section and footer links.

## Hosting Suggestions

Since Heroku no longer offers a free tier, here are the best free/low-cost alternatives for hosting this Django application:

### 1. PythonAnywhere (Recommended for Beginners)
- **Free Tier**: Basic free tier available.
- **Pros**: Very easy to set up for Django, persistent filesystem (good for SQLite), no sleep/spin-down.
- **Cons**: Free tier has limited bandwidth and no custom domain support.
- **Setup**:
    1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/).
    2. Upload your code (git clone).
    3. Set up a virtual environment.
    4. Configure the WSGI file (PythonAnywhere provides a GUI for this).
    5. Run `python manage.py migrate`.

### 2. Render (Modern Alternative)
- **Free Tier**: Free web services (spins down after inactivity).
- **Pros**: Modern workflow (git push to deploy), supports Docker.
- **Cons**: Free tier spins down (slow initial load), ephemeral filesystem (SQLite will be reset on every deploy/restart - **requires PostgreSQL** for persistence).
- **Note**: If using Render, you MUST switch back to PostgreSQL (Render offers a free PostgreSQL tier for 90 days, or you can use an external free DB like Neon or ElephantSQL).

### 3. Railway
- **Free Tier**: Trial credits, then pay-as-you-go.
- **Pros**: Excellent developer experience, fast builds.
- **Cons**: Not strictly "free" forever.

**Recommendation**: For a student project using SQLite, **PythonAnywhere** is the best choice as it supports SQLite persistence on the free tier. If you switch back to PostgreSQL, **Render** is a great modern option.
