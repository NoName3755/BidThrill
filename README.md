# BidThrill

## Overview
BidThrill is an e-commerce web application that allows users to create auction listings, place bids, leave comments, and manage watchlists. The project is built using Django for the backend and HTML & CSS for frontend.

## Features
- User authentication (login, logout, registration)
- Create, edit, and close auction listings
- Place bids on active listings
- Add comments on listings
- Watchlist functionality to track favorite listings
- Category-based filtering for browsing listings
- Automatic auction closure when the listing creator decides to end the auction
- User-friendly interface with real-time updates

## Technologies Used
- **Backend:** Django, Python, SQLite
- **Frontend:** HTML, CSS
- **Authentication:** Django's built-in authentication system
- **Data Fetching:** Django ORM

## Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/NoName3755/BidThrill.git
   cd BidThrill
   ```
2. **Apply database migrations:**
   ```sh
   python manage.py migrate
   ```
3. **Create a superuser (for admin access):**
   ```sh
   python manage.py createsuperuser
   ```
4. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
5. **Access the application:**
   Open `http://127.0.0.1:8000/` in your browser.

## Usage
- Register and log in to create and participate in auctions.
- Browse available auction listings and place bids.
- Comment on listings to engage with other users.
- Add listings to your watchlist for easy tracking.
- Close auctions when you're ready to finalize the sale.

## Future Improvements
- Implement real-time bid updates using WebSockets.
- Enhance UI with a more modern design.
- Add email notifications for bid updates and auction closures.
- Improve search and filtering functionalities.
