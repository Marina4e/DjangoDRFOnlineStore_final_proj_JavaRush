Используй Hop & Barley только как reference.
Не копируй старый frontend напрямую.
Создай новый frontend на Django Templates + HTMX + Alpine.js + Tailwind CSS.
--------------------

The project includes the layout and client-side logic for the following pages and components:

-   **Homepage (`home.html`):** a product catalog with interactive filters.
-   **Product Pages:** 12 unique pages for each product, complete with descriptions, specifications, and user reviews.
-   **Shopping Cart (`cart.html`):** an interactive cart with features to change item quantities and remove items, with automatic total recalculation.
-   **Checkout (`checkout.html`):** a form for entering shipping information and selecting a payment method.
-   **Authentication:**
    -   Login (`login.html`), registration (`register.html`), and password recovery (`forgot_password.html`) pages.
    -   **Login/Logout Simulation:** the header dynamically changes based on the user's authentication status (using `localStorage`).
-   **User Account (`account.html`):** a tabbed page for viewing order history and editing user information.
-   **Custom Admin Panel:**
    -   A page to view the product list (`admin/products.html`).
    -   A form to add/edit products (`admin/add.html`) with an image upload simulation.


--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/account.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Account | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="account-page-wrapper">
  <div class="account-container">
    <!-- Tabs Navigation -->
    <div class="account-tabs">
      <button class="account-tab active" data-tab-target="#order-history">Order History</button>
      <button class="account-tab" data-tab-target="#account-info">Account Information</button>
    </div>

    <!-- Tabs Content -->
    <div class="tab-content">
      <!-- Order History Panel -->
      <div id="order-history" class="tab-pane active">
        <div class="order-history-table">
          <!-- Table Header -->
          <div class="order-table-header">
            <div class="order-table-cell">Order Details</div>
            <div class="order-table-cell">Order Status</div>
            <div class="order-table-cell">Total</div>
          </div>
          <!-- Table Body -->
          <div class="order-table-body">
            <!-- Example Row 1 -->
            <div class="order-table-row">
              <div class="order-table-cell">
                <span class="order-id">#123232122033</span>
                <span class="order-date">7 Mar 2025</span>
              </div>
              <div class="order-table-cell">
                <span class="order-status">Pending</span>
              </div>
              <div class="order-table-cell">
                <span class="order-total">$100.00</span>
              </div>
            </div>
            <!-- Example Row 2 -->
            <div class="order-table-row">
              <div class="order-table-cell">
                <span class="order-id">#123232122033</span>
                <span class="order-date">7 Mar 2025</span>
              </div>
              <div class="order-table-cell">
                <span class="order-status">Pending</span>
              </div>
              <div class="order-table-cell">
                <span class="order-total">$90.00</span>
              </div>
            </div>
            <!-- ... add more rows as needed ... -->
            <div class="order-table-row">
              <div class="order-table-cell">
                <span class="order-id">#123232122033</span>
                <span class="order-date">7 Mar 2025</span>
              </div>
              <div class="order-table-cell">
                <span class="order-status">Confirmed</span>
              </div>
              <div class="order-table-cell">
                <span class="order-total">$140.00</span>
              </div>
            </div>
            <div class="order-table-row">
              <div class="order-table-cell">
                <span class="order-id">#123232122033</span>
                <span class="order-date">7 Mar 2025</span>
              </div>
              <div class="order-table-cell">
                <span class="order-status">Delivered</span>
              </div>
              <div class="order-table-cell">
                <span class="order-total">$120.00</span>
              </div>
            </div>
            <div class="order-table-row">
              <div class="order-table-cell">
                <span class="order-id">#123232122033</span>
                <span class="order-date">7 Mar 2025</span>
              </div>
              <div class="order-table-cell">
                <span class="order-status">Shipped</span>
              </div>
              <div class="order-table-cell">
                <span class="order-total">$120.00</span>
              </div>
            </div>
            <div class="order-table-row">
              <div class="order-table-cell">
                <span class="order-id">#123232122033</span>
                <span class="order-date">7 Mar 2025</span>
              </div>
              <div class="order-table-cell">
                <span class="order-status">Shipped</span>
              </div>
              <div class="order-table-cell">
                <span class="order-total">$120.00</span>
              </div>
            </div>
            <div class="order-table-row">
              <div class="order-table-cell">
                <span class="order-id">#123232122033</span>
                <span class="order-date">7 Mar 2025</span>
              </div>
              <div class="order-table-cell">
                <span class="order-status">Shipped</span>
              </div>
              <div class="order-table-cell">
                <span class="order-total">$120.00</span>
              </div>
            </div>
            <div class="order-table-row">
              <div class="order-table-cell">
                <span class="order-id">#123232122033</span>
                <span class="order-date">7 Mar 2025</span>
              </div>
              <div class="order-table-cell">
                <span class="order-status">Shipped</span>
              </div>
              <div class="order-table-cell">
                <span class="order-total">$120.00</span>
              </div>
            </div>
          </div>
        </div>
        <!-- Pagination (simplified) -->
        <div class="account-pagination">
          <a href="#" class="pagination-link-account disabled">← Previous</a>
          <a href="#" class="pagination-link-account">Next →</a>
        </div>
      </div>

      <!-- Account Information Panel -->
      <div id="account-info" class="tab-pane">
        <div class="account-form-container">
          <h2 class="account-form-title">Personal Info</h2>
          <form id="account-info-form">
            <div class="checkout-form-group">
              <label for="acc-full-name">Full Name</label>
              <input type="text" id="acc-full-name" name="full_name" class="Input" placeholder="Value" required>
            </div>
            <div class="checkout-form-group">
              <label for="acc-phone">Phone number</label>
              <input type="tel" id="acc-phone" name="phone" class="Input" placeholder="Value" required>
            </div>
            <div class="checkout-form-group">
              <label for="acc-email">Email</label>
              <input type="email" id="acc-email" name="email" class="Input" placeholder="example@mail.com" required>
            </div>
            <div class="checkout-form-group">
              <label for="acc-city">City</label>
              <input type="text" id="acc-city" name="city" class="Input" placeholder="Value" required>
            </div>
            <div class="checkout-form-group">
              <label for="acc-address">Shipping address</label>
              <textarea id="acc-address" name="address" class="Textarea" placeholder="Value" rows="3" required></textarea>
            </div>
            <button type="submit" class="button button--primary button--full-width">Save</button>
            <a href="#" class="button button--secondary button--full-width" id="logout-button">Logout</a>
          </form>
        </div>
      </div>

    </div>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/cart.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shopping Cart | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="cart-page-wrapper">
  <div class="cart-container">
    <h1 class="cart-title">Shopping Cart</h1>

    <div class="cart-items-list" id="cart-items-list">
      <!-- Cart Item 1 -->
      <div class="cart-item" data-price="5.99">
        <img src="../static/img/products/citra_hops.jpg" alt="Citra Hops" class="cart-item__image">
        <div class="cart-item__body">
          <div class="cart-item__details">
            <h2 class="cart-item__name">Citra Hops</h2>
            <div class="cart-item__price-info">
              <p class="cart-item__price" data-item-total-price>
                $29.95
              </p>
              <span class="cart-item__price-tag">per 100g</span>
            </div>
          </div>
          <div class="cart-item__actions">
            <div class="cart-item__quantity-selector">
              <button class="quantity-btn-cart" data-action="decrease"><i class="fa-solid fa-minus"></i></button>
              <span class="quantity-value-cart">5</span>
              <button class="quantity-btn-cart" data-action="increase"><i class="fa-solid fa-plus"></i></button>
            </div>
            <button class="button--remove" data-action="remove">
              Remove <i class="fa-solid fa-xmark"></i>
            </button>
          </div>
        </div>
      </div>

      <!-- Cart Item 2 -->
      <div class="cart-item" data-price="3.00">
        <img src="../static/img/products/caramel_malt.jpg" alt="Caramel Malt 60L" class="cart-item__image">
        <div class="cart-item__body">
          <div class="cart-item__details">
            <h2 class="cart-item__name">Caramel Malt 60L</h2>
            <div class="cart-item__price-info">
              <p class="cart-item__price" data-item-total-price>
                $3.00
              </p>
              <span class="cart-item__price-tag">per 1 lb</span>
            </div>
          </div>
          <div class="cart-item__actions">
            <div class="cart-item__quantity-selector">
              <button class="quantity-btn-cart" data-action="decrease"><i class="fa-solid fa-minus"></i></button>
              <span class="quantity-value-cart">1</span>
              <button class="quantity-btn-cart" data-action="increase"><i class="fa-solid fa-plus"></i></button>
            </div>
            <button class="button--remove" data-action="remove">
              Remove <i class="fa-solid fa-xmark"></i>
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="cart-summary">
      <div class="cart-summary__total">
        <p>Total</p>
        <p id="cart-total-price">$32.95</p>
      </div>
      <a href="checkout.html" class="button button--primary button--checkout">Proceed to Checkout</a>
    </div>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/checkout.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout | Hop & Barley</title>

    <!-- Google Fonts & Font Awesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Main CSS -->
    <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
    <div class="header-container">
        <a href="home.html" class="header__logo">
            <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
            <p class="logo-text">Hop & Barley</p>
        </a>
        <nav class="header__nav">
            <ul>
                <li><a href="home.html">Products</a></li>
                <li><a href="guides-recipes.html">Guides & Recipes</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">Resources</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <div class="header__auth-buttons" id="auth-guest">
            <a href="login.html" class="button button--secondary">Sign in</a>
            <a href="register.html" class="button button--primary">Register</a>
        </div>
        <div class="header__user-actions" id="auth-user">
            <a href="account.html" class="user-icon" aria-label="My Account">
                <img src="../static/img/icons/User_alt.svg" alt="User Account">
            </a>
            <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
                <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
            </a>

        </div>
    </div>
</header>

<!-- Main Content -->
<main class="checkout-page-wrapper">
    <div class="checkout-container">
        <h1 class="checkout-title">Order Details</h1>

        <form id="checkout-form">
            <!-- Shipping Information -->
            <section class="checkout-section">
                <h2 class="checkout-section__title">Shipping information</h2>
                <div class="checkout-form-group">
                    <label for="full-name">Full Name</label>
                    <input type="text" id="full-name" name="full_name" class="Input" placeholder="Value"  required>
                </div>
                <div class="checkout-form-group">
                    <label for="phone">Phone number</label>
                    <input type="tel" id="phone" name="phone" class="Input" placeholder="Value" required>
                </div>
                <div class="checkout-form-group">
                    <label for="city">City</label>
                    <input type="text" id="city" name="city" class="Input" placeholder="Value" required>
                </div>
                <div class="checkout-form-group">
                    <label for="address">Shipping address</label>
                    <textarea id="address" name="address" class="Textarea" placeholder="Value" rows="3" required></textarea>
                </div>
            </section>

            <!-- Payment Method -->
            <section class="checkout-section">
                <h2 class="checkout-section__title">Payment Method</h2>
                <div class="payment-options">
                    <label class="radio-option">
                        <input type="radio" name="payment_method" value="debit" checked>
                        <span class="radio-custom"></span>
                        <span class="radio-label">Debit Card</span>
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="payment_method" value="wallet">
                        <span class="radio-custom"></span>
                        <span class="radio-label">Digital Wallet</span>
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="payment_method" value="cod">
                        <span class="radio-custom"></span>
                        <span class="radio-label">Cash On Delivery</span>
                    </label>
                </div>
            </section>

            <!-- Order Summary -->
            <section class="checkout-summary">
                <h2 class="checkout-section__title">Order Summary</h2>
                <div class="summary-details">
                    <div class="summary-total">
                        <p>Total</p>
                        <p>$32.95</p>
                    </div>
                    <button type="submit" class="button button--primary button--pay">Pay</button>
                </div>
            </section>
        </form>
    </div>
</main>

<!-- Footer -->
<footer>
    <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
    <nav class="footer__nav">
        <ul>
            <li><a href="#">Contact</a></li>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Community</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">License</a></li>
        </ul>
    </nav>
    <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/forgot_password.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Forgot Password | Hop & Barley</title>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Font Awesome CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Link to your main CSS file -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>

    <!-- Block for unauthorized user -->
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>

    <!-- Block for authorized user -->
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="auth-page-wrapper">
  <div class="auth-background">
    <img src="../static/img/background/pattern.jpg" alt="Background pattern">
  </div>
  <div class="auth-form-container">
    <div class="auth-container auth-container--forgot-password">
      <form class="auth-form" id="forgot-password-form">
        <div class="InputField">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" class="Input" placeholder="Value" required>
        </div>

        <div class="ButtonGroup ButtonGroup--center">
          <a href="login.html" class="button button--cancel">Cancel</a>
          <button type="submit" class="button button--primary">Reset Password</button>
        </div>
      </form>
    </div>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- Link to your main JavaScript file -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/guides-recipes.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Guides & Recipes | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>
    </div>
  </div>
</header>

<!-- Main Content -->
<main class="static-page-wrapper">
  <div class="container">
    <div class="static-page-content">
      <h1 class="static-page-title">Guides & Recipes</h1>
      <p class="static-page-subtitle">Coming Soon!</p>
      <div class="static-page-text">
        <p>We are working hard to bring you the best guides and tested recipes from the world of homebrewing.</p>
        <p>Here you will find everything from beginner's guides on your first brew to advanced techniques for experienced brewers, as well as a collection of recipes for various beer styles using our products.</p>
        <p>Stay tuned for updates!</p>
      </div>
      <a href="home.html" class="button button--primary">Back to Products</a>
    </div>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/home.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Каталог товаров | Hop & Barley</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

    <!-- Font Awesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Link to your main CSS file -->
    <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
    <div class="header-container">
        <a href="home.html" class="header__logo">
            <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
            <p class="logo-text">Hop & Barley</p>
        </a>
        <nav class="header__nav">
            <ul>
                <li><a href="home.html">Products</a></li>
                <li><a href="guides-recipes.html">Guides & Recipes</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">Resources</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>

        <!-- Block for unauthorized user -->
        <div class="header__auth-buttons" id="auth-guest">
            <a href="login.html" class="button button--secondary">Sign in</a>
            <a href="register.html" class="button button--primary">Register</a>
        </div>

        <!-- Block for authorized user -->
        <div class="header__user-actions" id="auth-user">
            <a href="account.html" class="user-icon" aria-label="My Account">
                <img src="../static/img/icons/User_alt.svg" alt="User Account">
            </a>
            <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
                <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
            </a>

        </div>
    </div>
</header>

<!-- Main Content -->
<main>
    <section class="hero-banner">
        <img src="../static/img/background/hopfen-fields.jpg" alt="Beautiful hops on a dark background" class="hero-banner__image">
        <div class="hero-banner__overlay"></div>
    </section>

    <div class="container main-content-grid">
        <aside class="sidebar filter-menu">
            <div class="sidebar__section">
                <h3 class="section-title">Keywords</h3>
                <div class="keywords-list">
                </div>
            </div>

            <div class="sidebar__section">
                <h3 class="section-title">Product Type</h3>
                <div class="checkbox-group">
                    <label class="checkbox-container">Hops
                        <input type="checkbox" data-keyword="Hops">
                        <span class="checkmark"></span>
                    </label>
                    <label class="checkbox-container">Malts
                        <input type="checkbox" data-keyword="Malts">
                        <span class="checkmark"></span>
                    </label>
                    <label class="checkbox-container">Yeast
                        <input type="checkbox" data-keyword="Yeast">
                        <span class="checkmark"></span>
                    </label>
                    <label class="checkbox-container">Adjuncts
                        <input type="checkbox" data-keyword="Adjuncts">
                        <span class="checkmark"></span>
                    </label>
                </div>
            </div>
        </aside>

        <section class="products-area product-grid-section">
            <div class="search-sort-bar">
                <div class="search-input-wrapper">
                    <input type="text" placeholder="Search" class="search-input">
                    <button class="search-button" aria-label="Search">
                        <i class="fa-solid fa-magnifying-glass"></i>
                    </button>
                </div>
                <div class="sort-options">
                    <button class="sort-button active-sort">
                        <span>New</span>
                    </button>
                    <button class="sort-button">Price ascending</button>
                    <button class="sort-button">Price descending</button>
                    <button class="sort-button">Rating</button>
                </div>
            </div>

            <div class="product-grid">
                <!-- Card 1: Citra Hops -->
                <a href="product-citra-hops.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/citra_hops.jpg" alt="Citra Hops" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Citra Hops</h4>
                            <p class="product-card__price">$5.99</p>
                            <p class="product-card__description">Ideal for IPAs and Pale Ales</p>
                        </div>
                    </div>
                </a>

                <!-- Card 2: Maris Otter Pale Malt -->
                <a href="product-maris-otter-malt.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/maris_otter_malt.jpg" alt="Maris Otter Pale Malt" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Maris Otter Pale Malt</h4>
                            <p class="product-card__price">$2.50</p>
                            <p class="product-card__description">Perfect for traditional ales</p>
                        </div>
                    </div>
                </a>

                <!-- Card 3: SafAle US-05 Dry Ale Yeast -->
                <a href="product-safale-us05-yeast.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/safale_us05_yeast.jpg" alt="SafAle US-05 Dry Ale Yeast" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">SafAle US-05 Dry Ale Yeast</h4>
                            <p class="product-card__price">$3.25</p>
                            <p class="product-card__description">Clean fermenting American ale yeast</p>
                        </div>
                    </div>
                </a>

                <!-- Card 4: Cascade Hops -->
                <a href="product-cascade-hops.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/cascade_hops.jpg" alt="Cascade Hops" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Cascade Hops</h4>
                            <p class="product-card__price">$7.49</p>
                            <p class="product-card__description">Great for dry hopping</p>
                        </div>
                    </div>
                </a>

                <!-- Card 5: Caramel Malt 60L -->
                <a href="product-caramel-malt.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/caramel_malt.jpg" alt="Caramel Malt 60L" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Caramel Malt 60L</h4>
                            <p class="product-card__price">$3.00</p>
                            <p class="product-card__description">Head retention in darker beers</p>
                        </div>
                    </div>
                </a>

                <!-- Card 6: Saaz Hops -->
                <a href="product-saaz-hops.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/saaz_hops.jpg" alt="Saaz Hops" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Saaz Hops</h4>
                            <p class="product-card__price">$4.75</p>
                            <p class="product-card__description">Essential for Lagers</p>
                        </div>
                    </div>
                </a>

                <!-- Card 7: Pilsner Malt -->
                <a href="product-pilsner-malt.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/pilsner_malt.jpg" alt="Pilsner Malt" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Pilsner Malt</h4>
                            <p class="product-card__price">$2.20</p>
                            <p class="product-card__description">Foundation for lagers and pilsners</p>
                        </div>
                    </div>
                </a>

                <!-- Card 8: Imperial Organic Yeast A07 -->
                <a href="product-imperial-yeast.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/imperial_yeast.jpg" alt="Imperial Organic Yeast A07" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Imperial Organic Yeast A07</h4>
                            <p class="product-card__price">$8.99</p>
                            <p class="product-card__description">American ales with citrus notes</p>
                        </div>
                    </div>
                </a>

                <!-- Card 9: Centennial Hops -->
                <a href="product-centennial-hops.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/centennial_hops.jpg" alt="Centennial Hops" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Centennial Hops</h4>
                            <p class="product-card__price">$6.20</p>
                            <p class="product-card__description">Often called "Super Cascade"</p>
                        </div>
                    </div>
                </a>

                <!-- Card 10: Mosaic Hops-->
                <a href="product-mosaic-hops.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/mosaic_hops.jpg" alt="mosaic-hops" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Mosaic Hops</h4>
                            <p class="product-card__price">$9.50</p>
                            <p class="product-card__description">Ideal for IPAs and Pale Ales</p>
                        </div>
                    </div>
                </a>

                <!-- Card 11: West Coast IPA - All-Grain Kit -->
                <a href="product-west-coast-ipa-kit.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/ipa_kit.jpg" alt="West Coast IPA - All-Grain Kit" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">West Coast IPA - All-Grain Kit</h4>
                            <p class="product-card__price">$60</p>
                            <p class="product-card__description">West Coast IPA</p>
                        </div>
                    </div>
                </a>

                <!-- Card 12: Unmalted Whea -->
                <a href="product-unmalted-wheat.html" class="product-card-link">
                    <div class="product-card">
                        <img src="../static/img/products/unmalted_wheat.jpg" alt="Blanche Malt" class="product-card__image">
                        <div class="product-card__info">
                            <h4 class="product-card__name">Unmalted Wheat</h4>
                            <p class="product-card__price">$1.80</p>
                            <p class="product-card__description">Belgian Witbier</p>
                        </div>
                    </div>
                </a>
            </div>

            <div class="pagination">
                <a href="#" class="pagination__link pagination__link--prev">
                    <i class="fa-solid fa-arrow-left"></i>
                    <span>Previous</span>
                </a>
                <div class="pagination-list">
                    <a href="#" class="pagination__link active">1</a>
                    <a href="#" class="pagination__link">2</a>
                    <a href="#" class="pagination__link">3</a>
                    <span class="pagination__dots">...</span>
                    <a href="#" class="pagination__link">20</a>
                </div>
                <a href="#" class="pagination__link pagination__link--next">
                    <span>Next</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </a>
            </div>
        </section>
    </div>
</main>

<!-- Footer -->
<footer>
    <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
    <nav class="footer__nav">
        <ul>
            <li><a href="#">Contact</a></li>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Community</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">License</a></li>
        </ul>
    </nav>
    <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/login.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sign In | Hop & Barley</title>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Font Awesome CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Link to your main CSS file -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>

    <!-- Block for unauthorized user -->
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>

    <!-- Block for authorized user -->
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="auth-page-wrapper">
  <div class="auth-background">
    <img src="../static/img/background/pattern.jpg" alt="Background pattern">
  </div>
  <div class="auth-form-container">
    <div class="auth-container auth-container--login">
      <div class="Legend">
        <h1 class="auth-title">Sign In</h1>
      </div>

      <form class="auth-form" id="login-form">
        <div class="InputField">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" class="Input" placeholder="Value" required>
        </div>
        <div class="InputField">
          <label for="password">Password</label>
          <input type="password" id="password" name="password" class="Input" placeholder="Value" required>
        </div>

        <div class="ButtonGroup">
          <button type="submit" class="button button--primary">Sign In</button>
        </div>

        <div class="TextLink">
          <a href="forgot_password.html">Forgot password?</a>
        </div>
      </form>

      <p class="auth-switch">Don’t have an account? <a href="register.html">Sign up</a></p>
    </div>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- Link to your main JavaScript file -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-caramel-malt.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Caramel Malt 60L | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="page-product">
  <div class="container">
    <!-- Product Info Section -->
    <section class="product-details-section">
      <div class="product-image-container">
        <img src="../static/img/products/caramel_malt.jpg" alt="Caramel Malt 60L" class="product-image">
      </div>
      <div class="product-info-column">
        <div class="product-title-price">
          <h1 class="product-name">Caramel Malt 60L</h1>
          <div class="price-section">
            <span class="price-tag">per 1 lb</span>
            <p class="product-price">$3.00</p>
          </div>
        </div>
        <div class="product-description">
          <p>Caramel Malt 60L (also known as Crystal 60L) is a versatile specialty malt that is a secret weapon for many brewers to enhance beer color, flavor, and body. It imparts a beautiful copper-amber hue to the brew.</p>
          <p>The flavor of this malt is characterized by distinct notes of caramel, toffee, and light hints of toasted bread. It adds a pleasant sweetness to the beer that beautifully balances hop bitterness and also contributes to improved head retention.</p>
          <p>Caramel Malt 60L is ideal for a wide range of styles, from Pale Ales and Amber Ales to Porters and Stouts, adding complexity and depth.</p>
        </div>
        <div class="cart-controls">
          <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
            <i class="fa-solid fa-cart-shopping"></i>
            <span>Add to Cart</span>
          </button>
          <div class="quantity-counter is-hidden" id="quantity-counter">
            <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
            <span class="quantity-value">1 in cart</span>
            <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Technical Specifications Accordion -->
    <section class="accordion-section">
      <div class="accordion-item">
        <div class="accordion-title">
          <h3>Technical Specifications</h3>
          <i class="fa-solid fa-chevron-down accordion-icon"></i>
        </div>
        <div class="accordion-content">
          <ul>
            <li><strong>Origin:</strong> USA / Belgium</li>
            <li><strong>Type:</strong> Crystal/Caramel Malt</li>
            <li><strong>Color (°L):</strong> 60 °L</li>
            <li><strong>Moisture:</strong> 5.0% max</li>
            <li><strong>Extract FG, Dry:</strong> 75%</li>
            <li><strong>Flavor Profile:</strong> Sweet, caramel, toffee, hints of toasted bread</li>
            <li><strong>Usage:</strong> Typically 3-15% of the grist</li>
            <li><strong>Recommended Beer Styles:</strong> Pale Ale, Amber Ale, IPA, Brown Ale, Porter, Stout, Scotch Ale</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Latest Reviews Section -->
    <section class="reviews-section">
      <h2 class="reviews-title">Latest reviews</h2>
      <div class="reviews-grid">
        <!-- Review Card 1 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">The Perfect Sweet Spot</h4>
            <p class="review-text">60L is my favorite caramel malt. It's not too light and not too dark. It provides the perfect balance of sweetness and caramel flavor for my Amber Ales. The color comes out just gorgeous.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar1.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">AmberAleFanatic</span>
          </div>
        </div>
        <!-- Review Card 2 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Never Brew Without It</h4>
            <p class="review-text">I add a bit of C60 to almost every recipe. It improves head retention and gives the beer a finished quality that's hard to achieve otherwise. Works great in IPAs to balance the bitterness.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar2.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">BrewMore</span>
          </div>
        </div>
        <!-- Review Card 3 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Consistent and Reliable</h4>
            <p class="review-text">The quality of this malt is always top-notch. Consistent color, wonderful aroma when crushed. If a recipe calls for Crystal 60, this is the one I always reach for. Recommended.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar3.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">ConsistentBrewer</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-cascade-hops.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cascade Hops | Hop & Barley</title>

    <!-- Google Fonts & Font Awesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Main CSS -->
    <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
    <div class="header-container">
        <a href="home.html" class="header__logo">
            <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
            <p class="logo-text">Hop & Barley</p>
        </a>
        <nav class="header__nav">
            <ul>
                <li><a href="home.html">Products</a></li>
                <li><a href="guides-recipes.html">Guides & Recipes</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">Resources</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <div class="header__auth-buttons" id="auth-guest">
            <a href="login.html" class="button button--secondary">Sign in</a>
            <a href="register.html" class="button button--primary">Register</a>
        </div>
        <div class="header__user-actions" id="auth-user">
            <a href="account.html" class="user-icon" aria-label="My Account">
                <img src="../static/img/icons/User_alt.svg" alt="User Account">
            </a>
            <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
                <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
            </a>

        </div>
    </div>
</header>

<!-- Main Content -->
<main class="page-product">
    <div class="container">
        <!-- Product Info Section -->
        <section class="product-details-section">
            <div class="product-image-container">
                <img src="../static/img/products/cascade_hops.jpg" alt="Cascade Hops" class="product-image">
            </div>
            <div class="product-info-column">
                <div class="product-title-price">
                    <h1 class="product-name">Cascade Hops</h1>
                    <div class="price-section">
                        <span class="price-tag">per 100g</span>
                        <p class="product-price">$7.49</p>
                    </div>
                </div>
                <div class="product-description">
                    <p>Cascade is arguably the most famous hop in the American craft brewing revolution. Developed in Oregon, it has a unique floral and citrus character that defined the taste of the classic American Pale Ale.</p>
                    <p>Its moderate bitterness and vibrant aroma, with notes of grapefruit, orange, and light floral undertones, make it incredibly versatile. Cascade is excellent for both bittering and late kettle additions or for dry hopping.</p>
                    <p>This hop is a reliable choice for brewers looking to create a refreshing, balanced, and recognizable ale.</p>
                </div>
                <div class="cart-controls">
                    <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
                        <i class="fa-solid fa-cart-shopping"></i>
                        <span>Add to Cart</span>
                    </button>
                    <div class="quantity-counter is-hidden" id="quantity-counter">
                        <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
                        <span class="quantity-value">1 in cart</span>
                        <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
                    </div>
                </div>
            </div>
        </section>

        <!-- Technical Specifications Accordion -->
        <section class="accordion-section">
            <div class="accordion-item">
                <div class="accordion-title">
                    <h3>Technical Specifications</h3>
                    <i class="fa-solid fa-chevron-down accordion-icon"></i>
                </div>
                <div class="accordion-content">
                    <ul>
                        <li><strong>Origin:</strong> USA</li>
                        <li><strong>Type:</strong> Aroma (Dual-Purpose)</li>
                        <li><strong>Alpha Acids:</strong> 4.5% - 7.0%</li>
                        <li><strong>Beta Acids:</strong> 4.5% - 7.0%</li>
                        <li><strong>Aroma Profile:</strong> Medium-intensity floral, citrus (grapefruit), and spicy notes.</li>
                        <li><strong>Cohumulone:</strong> 33% - 40%</li>
                        <li><strong>Total Oil:</strong> 0.8 - 1.5 mL/100g</li>
                        <li><strong>Recommended Beer Styles:</strong> American Pale Ale, IPA, Porter, Barleywine, Witbier</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Latest Reviews Section -->
        <section class="reviews-section">
            <h2 class="reviews-title">Latest reviews</h2>
            <div class="reviews-grid">
                <!-- Review Card 1 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">The Classic APA Hop</h4>
                        <p class="review-text">If you're brewing an American Pale Ale, you simply have to use Cascade. It's a classic. Bright, citrusy, refreshing. Never fails. Opens up beautifully on the dry hop.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar8.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">PaleAlePete</span>
                    </div>
                </div>
                <!-- Review Card 2 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">My Go-To Aroma Hop</h4>
                        <p class="review-text">I add Cascade to almost all of my light ales for aroma. It gives the beer that signature character everyone loves. The fresh harvest smells absolutely divine!</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar9.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">AromaAddict</span>
                    </div>
                </div>
                <!-- Review Card 3 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">Solid and Dependable</h4>
                        <p class="review-text">A good, reliable hop. Not as "explosive" as Citra or Mosaic, but for a balanced beer, it's just what you need. Sometimes the alpha acids are on the lower end, so check the batch specs. Otherwise, excellent.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar10.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">BrewAnalyst</span>
                    </div>
                </div>
            </div>
        </section>
    </div>
</main>

<!-- Footer -->
<footer>
    <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
    <nav class="footer__nav">
        <ul>
            <li><a href="#">Contact</a></li>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Community</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">License</a></li>
        </ul>
    </nav>
    <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-centennial-hops.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Centennial Hops | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="page-product">
  <div class="container">
    <!-- Product Info Section -->
    <section class="product-details-section">
      <div class="product-image-container">
        <img src="../static/img/products/centennial_hops.jpg" alt="Centennial Hops" class="product-image">
      </div>
      <div class="product-info-column">
        <div class="product-title-price">
          <h1 class="product-name">Centennial Hops</h1>
          <div class="price-section">
            <span class="price-tag">per 100g</span>
            <p class="product-price">$6.20</p>
          </div>
        </div>
        <div class="product-description">
          <p>Centennial is a classic American hop often referred to as "Super Cascade" due to its similar citrus profile but with a higher intensity and alpha acid content. It is one of the "Three Cs" (along with Cascade and Columbus) that defined the flavor of American IPAs.</p>
          <p>The aroma of Centennial is powerful, with bright notes of lemon, grapefruit, and pronounced floral undertones. Unlike Cascade, it is less spicy and more "clean" in its citrus expression. Thanks to its high alpha acid content, it is excellent for both bittering and creating an intense aroma.</p>
          <p>This is an extremely versatile hop, perfect for American Pale Ales, IPAs, and Double IPAs, giving them a bright and recognizable character.</p>
        </div>
        <div class="cart-controls">
          <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
            <i class="fa-solid fa-cart-shopping"></i>
            <span>Add to Cart</span>
          </button>
          <div class="quantity-counter is-hidden" id="quantity-counter">
            <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
            <span class="quantity-value">1 in cart</span>
            <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Technical Specifications Accordion -->
    <section class="accordion-section">
      <div class="accordion-item">
        <div class="accordion-title">
          <h3>Technical Specifications</h3>
          <i class="fa-solid fa-chevron-down accordion-icon"></i>
        </div>
        <div class="accordion-content">
          <ul>
            <li><strong>Origin:</strong> USA</li>
            <li><strong>Type:</strong> Dual-Purpose</li>
            <li><strong>Alpha Acids:</strong> 9.0% - 11.5%</li>
            <li><strong>Beta Acids:</strong> 3.5% - 4.5%</li>
            <li><strong>Aroma Profile:</strong> Intense floral and citrus (lemon, grapefruit).</li>
            <li><strong>Cohumulone:</strong> 28% - 30%</li>
            <li><strong>Total Oil:</strong> 1.5 - 2.5 mL/100g</li>
            <li><strong>Recommended Beer Styles:</strong> All US Ale styles, especially IPA, Double IPA, and American Pale Ale.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Latest Reviews Section -->
    <section class="reviews-section">
      <h2 class="reviews-title">Latest reviews</h2>
      <div class="reviews-grid">
        <!-- Review Card 1 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Super Cascade Indeed!</h4>
            <p class="review-text">The name says it all. It's like Cascade, but better. More citrus, more bitterness, more everything. Perfect for a single-hop IPA. One of my all-time favorite hops.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar3.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">IPA_Fan</span>
          </div>
        </div>
        <!-- Review Card 2 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Clean Bitterness</h4>
            <p class="review-text">I use Centennial for the main bittering in my IPAs. It provides a very clean, smooth bitterness without the harshness that can sometimes come from other high-alpha varieties. And the whirlpool aroma is fantastic.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar4.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">BitterIsBetter</span>
          </div>
        </div>
        <!-- Review Card 3 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">A Classic for a Reason</h4>
            <p class="review-text">You can't go wrong with Centennial. It's a time-tested, reliable hop. Perfect for a classic West Coast IPA. Always delivers predictable and excellent results.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar5.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">WestCoastBrewer</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-citra-hops.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Citra Hops | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>

    <!-- Block for unauthorized user -->
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>

    <!-- Block for authorized user -->
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="page-product">
  <div class="container">
    <!-- Product Info Section -->
    <section class="product-details-section">
      <div class="product-image-container">
        <img src="../static/img/products/citra_hops.jpg" alt="Citra Hops" class="product-image">
      </div>
      <div class="product-info-column">
        <div class="product-title-price">
          <h1 class="product-name">Citra Hops</h1>
          <div class="price-section">
            <span class="price-tag">per 100g</span>
            <p class="product-price">$5.99</p>
          </div>
        </div>
        <div class="product-description">
          <p>Citra is one of the most sought-after and recognizable hop varieties in the world of craft brewing, famous for its bright and multifaceted citrus aroma. Developed in the USA, this variety is ideal for IPAs, Pale Ales, and other styles where a distinct fruity profile is desired.</p>
          <p>Citra boasts a high alpha acid content, making it excellent for both bitterness and intense aroma. It imparts notes of grapefruit, lime, passion fruit, lychee, and melon to beer, creating a unique tropical bouquet.</p>
          <p>Our T-90 pellets are hermetically sealed to preserve freshness and maximum aromatics.</p>
        </div>
        <!-- Container for managing the cart -->
        <div class="cart-controls">
          <!-- Add to Cart button (visible by default) -->
          <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
            <i class="fa-solid fa-cart-shopping"></i>
            <span>Add to Cart</span>
          </button>

          <!-- Quantity counter (hidden by default) -->
          <div class="quantity-counter is-hidden" id="quantity-counter">
            <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity">
              <i class="fa-solid fa-minus"></i>
            </button>
            <span class="quantity-value">1 in cart</span>
            <button class="quantity-btn" data-action="increase" aria-label="Increase quantity">
              <i class="fa-solid fa-plus"></i>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Technical Specifications Accordion -->
    <section class="accordion-section">
      <div class="accordion-item">
        <div class="accordion-title">
          <h3>Technical Specifications</h3>
          <i class="fa-solid fa-chevron-down accordion-icon"></i>
        </div>
        <div class="accordion-content">
          <ul>
            <li><strong>Origin:</strong> USA</li>
            <li><strong>Type:</strong> Aroma (Dual-Purpose)</li>
            <li><strong>Alpha Acids:</strong> 11.0% - 13.0%</li>
            <li><strong>Beta Acids:</strong> 3.0% - 4.5%</li>
            <li><strong>Aroma Profile:</strong> Grapefruit, Lime, Passion Fruit, Lychee, Melon</li>
            <li><strong>Usage:</strong> Late Kettle Addition, Dry Hopping</li>
            <li><strong>Recommended Beer Styles:</strong> IPA, Double IPA, Pale Ale, American Wheat</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Latest Reviews Section -->
    <section class="reviews-section">
      <h2 class="reviews-title">Latest reviews</h2>
      <div class="reviews-grid">
        <!-- Review Card 1 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Explosive Citrus Aroma!</h4>
            <p class="review-text">Used Citra for my latest NEIPA, and the aroma is absolutely incredible. Poured hazy, with intense notes of grapefruit and passion fruit. A must-have for any hop-forward beer!</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar1.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">Homebrewer_27</span>
          </div>
        </div>
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Great for Beginners</h4>
            <p class="review-text">When I was just starting to brew, this was the yeast recommended to me, and I have no regrets. It's very forgiving with temperature and handles many beginner mistakes.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar8.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">Homebr</span>
          </div>
        </div>
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Perfect  Citrus!</h4>
            <p class="review-text">The beer always turns out great. A must-have for any hop-forward beer!</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar2.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">r_27</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-imperial-yeast.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Imperial Organic Yeast A07 | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="page-product">
  <div class="container">
    <!-- Product Info Section -->
    <section class="product-details-section">
      <div class="product-image-container">
        <img src="../static/img/products/imperial_yeast.jpg" alt="Imperial Organic Yeast A07" class="product-image">
      </div>
      <div class="product-info-column">
        <div class="product-title-price">
          <h1 class="product-name">Imperial Organic Yeast A07</h1>
          <div class="price-section">
            <span class="price-tag">per pouch</span>
            <p class="product-price">$8.99</p>
          </div>
        </div>
        <div class="product-description">
          <p>Imperial Organic Yeast A07 "Flagship" is a versatile and extremely popular liquid yeast, known for its ability to create balanced ales with a light fruity character. This strain is a true workhorse and is perfect for most American beer styles.</p>
          <p>"Flagship" provides a clean fermentation with light ester notes of citrus and stone fruit that complement, rather than overpower, the hop and malt profile. It has good attenuation and moderate flocculation, leaving behind a soft and smooth mouthfeel.</p>
          <p>Thanks to the high cell count per package (200 billion), this yeast does not require a starter for most standard batches of beer, making it a convenient and reliable choice.</p>
        </div>
        <div class="cart-controls">
          <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
            <i class="fa-solid fa-cart-shopping"></i>
            <span>Add to Cart</span>
          </button>
          <div class="quantity-counter is-hidden" id="quantity-counter">
            <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
            <span class="quantity-value">1 in cart</span>
            <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Technical Specifications Accordion -->
    <section class="accordion-section">
      <div class="accordion-item">
        <div class="accordion-title">
          <h3>Technical Specifications</h3>
          <i class="fa-solid fa-chevron-down accordion-icon"></i>
        </div>
        <div class="accordion-content">
          <ul>
            <li><strong>Strain Type:</strong> Ale</li>
            <li><strong>Flocculation:</strong> Medium</li>
            <li><strong>Attenuation:</strong> 73-77%</li>
            <li><strong>Temperature Range:</strong> 62-72°F (17-22°C)</li>
            <li><strong>Alcohol Tolerance:</strong> 10% ABV</li>
            <li><strong>Flavor Profile:</strong> Balanced, slightly fruity, hints of citrus and stone fruit.</li>
            <li><strong>Cell Count:</strong> ~200 Billion Cells</li>
            <li><strong>Recommended Beer Styles:</strong> American Pale Ale, IPA, Double IPA, Porter, Stout, Amber Ale</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Latest Reviews Section -->
    <section class="reviews-section">
      <h2 class="reviews-title">Latest reviews</h2>
      <div class="reviews-grid">
        <!-- Review Card 1 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">My House Strain!</h4>
            <p class="review-text">I've tried many yeasts, but I always come back to A07. This is my "house" strain for all American ales. It's reliable, clean, and predictable. And the fact that you don't need a starter saves a ton of time!</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar10.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">HouseStrainGuy</span>
          </div>
        </div>
        <!-- Review Card 2 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Perfect for Hazy IPAs</h4>
            <p class="review-text">This yeast works great in NEIPAs. It leaves a bit of body and enhances the fruity notes of the hops, creating that "juicy" flavor. Highly recommend.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar1.jpg" alt="User avatar" class="author-avatar">
            <span class="author-name">HazyJane</span>
          </div>
        </div>
        <!-- Review Card 3 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Great, but temperature sensitive</h4>
            <p class="review-text">An excellent strain, it fermented my APA to perfection. The only thing is, try to keep the temperature at the lower end of the range. If it gets too warm, it can produce too many esters. But with proper control, the result is superb.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar2.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">TempControlFreak</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-maris-otter-malt.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maris Otter Pale Malt | Hop & Barley</title>

    <!-- Google Fonts & Font Awesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Main CSS -->
    <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
    <div class="header-container">
        <a href="home.html" class="header__logo">
            <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
            <p class="logo-text">Hop & Barley</p>
        </a>
        <nav class="header__nav">
            <ul>
                <li><a href="home.html">Products</a></li>
                <li><a href="guides-recipes.html">Guides & Recipes</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">Resources</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <div class="header__auth-buttons" id="auth-guest">
            <a href="login.html" class="button button--secondary">Sign in</a>
            <a href="register.html" class="button button--primary">Register</a>
        </div>
        <div class="header__user-actions" id="auth-user">
            <a href="account.html" class="user-icon" aria-label="My Account">
                <img src="../static/img/icons/User_alt.svg" alt="User Account">
            </a>
            <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
                <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
            </a>

        </div>
    </div>
</header>

<!-- Main Content -->
<main class="page-product">
    <div class="container">
        <!-- Product Info Section -->
        <section class="product-details-section">
            <div class="product-image-container">
                <img src="../static/img/products/maris_otter_malt.jpg" alt="Maris Otter Pale Malt" class="product-image">
            </div>
            <div class="product-info-column">
                <div class="product-title-price">
                    <h1 class="product-name">Maris Otter Pale Malt</h1>
                    <div class="price-section">
                        <span class="price-tag">per 1 lb</span>
                        <p class="product-price">$2.50</p>
                    </div>
                </div>
                <div class="product-description">
                    <p>Maris Otter Pale Malt is the cornerstone of British brewing heritage, a revered base malt prized by brewers worldwide for its exceptional quality and flavor.</p>
                    <p>It provides a rich, slightly sweet, and biscuity malt backbone that is more complex than standard 2-row malts, with subtle nutty undertones that enhance any beer style. Perfect for creating authentic British ales such as Bitters, IPAs, Porters, and Stouts.</p>
                    <p>Its excellent processing characteristics and high extract yield make it a reliable and efficient choice for both novice and experienced brewers.</p>
                </div>
                <div class="cart-controls">
                    <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
                        <i class="fa-solid fa-cart-shopping"></i>
                        <span>Add to Cart</span>
                    </button>
                    <div class="quantity-counter is-hidden" id="quantity-counter">
                        <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
                        <span class="quantity-value">1 in cart</span>
                        <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
                    </div>
                </div>
            </div>
        </section>

        <!-- Technical Specifications Accordion -->
        <section class="accordion-section">
            <div class="accordion-item">
                <div class="accordion-title">
                    <h3>Technical Specifications</h3>
                    <i class="fa-solid fa-chevron-down accordion-icon"></i>
                </div>
                <div class="accordion-content">
                    <ul>
                        <li><strong>Origin:</strong> United Kingdom</li>
                        <li><strong>Type:</strong> Base Malt</li>
                        <li><strong>Color (°L):</strong> 2.5 - 4.0 °L</li>
                        <li><strong>Moisture:</strong> 4.0% max</li>
                        <li><strong>Protein:</strong> 9.5% - 10.5%</li>
                        <li><strong>Diastatic Power:</strong> ≈ 120 °L</li>
                        <li><strong>Usage:</strong> Up to 100% of the grist</li>
                        <li><strong>Recommended Beer Styles:</strong> English Pale Ale, ESB, Bitter, Porter, Stout, Mild Ale</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Latest Reviews Section -->
        <section class="reviews-section">
            <h2 class="reviews-title">Latest reviews</h2>
            <div class="reviews-grid">
                <!-- Review Card 1 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">The Gold Standard!</h4>
                        <p class="review-text">Unbeatable flavor for my bitters. If you want to brew a real British ale, you have to start with this malt. Fantastic efficiency and a wonderful aroma during the mash. 10/10.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar2.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">UKAleMaster</span>
                    </div>
                </div>
                <!-- Review Card 2 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">Incredibly Reliable and Flavorful</h4>
                        <p class="review-text">I've been using this malt for years. It always crushes perfectly, gives predictable results, and lends a depth to the beer that you just can't find in other base malts. Perfect for porters.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar3.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">MashAndSparge</span>
                    </div>
                </div>
                <!-- Review Card 3 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">Adds Great Complexity</h4>
                        <p class="review-text">I usually use American 2-row, but decided to try Maris Otter for my pale ale. The difference is noticeable! It added pleasant biscuit notes. A bit more expensive, so 4 stars, but the flavor is a solid 5.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar4.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">CraftyBrewer_USA</span>
                    </div>
                </div>
            </div>
        </section>
    </div>
</main>

<!-- Footer -->
<footer>
    <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
    <nav class="footer__nav">
        <ul>
            <li><a href="#">Contact</a></li>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Community</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">License</a></li>
        </ul>
    </nav>
    <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-mosaic-hops.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mosaic Hops | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="page-product">
  <div class="container">
    <!-- Product Info Section -->
    <section class="product-details-section">
      <div class="product-image-container">
        <img src="../static/img/products/mosaic_hops.jpg" alt="Mosaic Hops" class="product-image">
      </div>
      <div class="product-info-column">
        <div class="product-title-price">
          <h1 class="product-name">Mosaic Hops</h1>
          <div class="price-section">
            <span class="price-tag">per 100g</span>
            <p class="product-price">$9.50</p>
          </div>
        </div>
        <div class="product-description">
          <p>Mosaic is one of the most vibrant and multifaceted hops on the modern craft scene. As a "daughter" of Simcoe, it inherited the best from its lineage and added a unique palette of aromas, making it a true aromatic bomb.</p>
          <p>The name "Mosaic" is fully justified: it creates a complex mosaic of flavors and aromas, including notes of tropical fruits (mango, guava), citrus (tangerine), berries (blueberry), stone fruits (peach), and even light pine and earthy undertones.</p>
          <p>This hop is ideal for dry hopping in IPA and Pale Ale styles, where it can unleash its full potential, creating a juicy, vibrant, and unforgettable beer.</p>
        </div>
        <div class="cart-controls">
          <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
            <i class="fa-solid fa-cart-shopping"></i>
            <span>Add to Cart</span>
          </button>
          <div class="quantity-counter is-hidden" id="quantity-counter">
            <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
            <span class="quantity-value">1 in cart</span>
            <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Technical Specifications Accordion -->
    <section class="accordion-section">
      <div class="accordion-item">
        <div class="accordion-title">
          <h3>Technical Specifications</h3>
          <i class="fa-solid fa-chevron-down accordion-icon"></i>
        </div>
        <div class="accordion-content">
          <ul>
            <li><strong>Origin:</strong> USA</li>
            <li><strong>Type:</strong> Dual-Purpose</li>
            <li><strong>Alpha Acids:</strong> 11.5% - 13.5%</li>
            <li><strong>Beta Acids:</strong> 3.2% - 3.9%</li>
            <li><strong>Aroma Profile:</strong> Complex and multifaceted. Tropical fruit (mango, guava), citrus (tangerine), berry (blueberry), stone fruit (peach), pine, and earthy notes.</li>
            <li><strong>Cohumulone:</strong> 24% - 26%</li>
            <li><strong>Total Oil:</strong> 1.0 - 1.5 mL/100g</li>
            <li><strong>Recommended Beer Styles:</strong> IPA, Double IPA, Hazy/NEIPA, American Pale Ale, Session IPA.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Latest Reviews Section -->
    <section class="reviews-section">
      <h2 class="reviews-title">Latest reviews</h2>
      <div class="reviews-grid">
        <!-- Review Card 1 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">A Flavor Explosion!</h4>
            <p class="review-text">If you want to brew a Hazy IPA that smells like a tropical fruit basket, Mosaic is your choice. Added it on the dry hop, and the result exceeded all expectations. Incredible!</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar6.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">HazyHead</span>
          </div>
        </div>
        <!-- Review Card 2 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">So Complex and Delicious</h4>
            <p class="review-text">This hop has it all! Every time I use it, I find new nuances—sometimes mango, sometimes blueberry, sometimes pine. It never gets old. Worth every penny.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar7.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">FlavorExplorer</span>
          </div>
        </div>
        <!-- Review Card 3 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">My Secret Weapon</h4>
            <p class="review-text">I love mixing Mosaic with Citra 1:1 for my DIPAs. They create the perfect tandem. Mosaic adds that "berry" complexity that Citra lacks. A true secret weapon.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar8.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">DIPA_Dan</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-pilsner-malt.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pilsner Malt | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="page-product">
  <div class="container">
    <!-- Product Info Section -->
    <section class="product-details-section">
      <div class="product-image-container">
        <img src="../static/img/products/pilsner_malt.jpg" alt="Pilsner Malt" class="product-image">
      </div>
      <div class="product-info-column">
        <div class="product-title-price">
          <h1 class="product-name">Pilsner Malt</h1>
          <div class="price-section">
            <span class="price-tag">per 1 lb</span>
            <p class="product-price">$2.20</p>
          </div>
        </div>
        <div class="product-description">
          <p>Pilsner Malt is the lightest base malt, forming the foundation for classic German and Czech pilsners, as well as a multitude of other light lagers and ales. It is produced from high-quality two-row barley and undergoes gentle kilning at low temperatures.</p>
          <p>This malt imparts a very light, straw-like color and a clean, slightly sweet, grainy flavor to the beer. Its neutral character allows the aroma of hops and the work of the yeast to fully express themselves, making it an ideal base for beers where purity and crispness are paramount.</p>
          <p>Thanks to its high enzymatic activity, Pilsner Malt is excellent for mashes with a large proportion of unmalted grains.</p>
        </div>
        <div class="cart-controls">
          <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
            <i class="fa-solid fa-cart-shopping"></i>
            <span>Add to Cart</span>
          </button>
          <div class="quantity-counter is-hidden" id="quantity-counter">
            <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
            <span class="quantity-value">1 in cart</span>
            <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Technical Specifications Accordion -->
    <section class="accordion-section">
      <div class="accordion-item">
        <div class="accordion-title">
          <h3>Technical Specifications</h3>
          <i class="fa-solid fa-chevron-down accordion-icon"></i>
        </div>
        <div class="accordion-content">
          <ul>
            <li><strong>Origin:</strong> Germany / Belgium</li>
            <li><strong>Type:</strong> Base Malt</li>
            <li><strong>Color (°L):</strong> 1.5 - 2.1 °L</li>
            <li><strong>Moisture:</strong> 4.5% max</li>
            <li><strong>Protein:</strong> 10.0% - 11.5%</li>
            <li><strong>Diastatic Power:</strong> > 100 °Lintner</li>
            <li><strong>Flavor Profile:</strong> Clean, light, sweet, grainy</li>
            <li><strong>Usage:</strong> Up to 100% of the grist</li>
            <li><strong>Recommended Beer Styles:</strong> Pilsner, Helles, Kolsch, Belgian Tripel, Light Lagers, Saison</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Latest Reviews Section -->
    <section class="reviews-section">
      <h2 class="reviews-title">Latest reviews</h2>
      <div class="reviews-grid">
        <!-- Review Card 1 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">The Heart of a Good Lager</h4>
            <p class="review-text">If you want to brew a true, crisp pilsner, you can't do without this malt. It provides that clean, light base on which everything else is built. Works perfectly.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar7.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">LagerLover</span>
          </div>
        </div>
        <!-- Review Card 2 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Clean Canvas</h4>
            <p class="review-text">I use this malt as a "clean canvas" for many of my varieties. It doesn't interfere, but only enhances the other ingredients. Ideal for experimenting with hops or yeast. The quality is always top-notch.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar8.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">TheMaltster</span>
          </div>
        </div>
        <!-- Review Card 3 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Very Light, Be Aware</h4>
            <p class="review-text">Excellent malt, but it's really very light. If you want any color at all, be sure to add specialty malts. For pilsners - it's super, but for pale ales I'd prefer something darker. Otherwise, no complaints.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar9.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">HomebrewHobbyist</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-saaz-hops.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saaz Hops | Hop & Barley</title>

    <!-- Google Fonts & Font Awesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Main CSS -->
    <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
    <div class="header-container">
        <a href="home.html" class="header__logo">
            <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
            <p class="logo-text">Hop & Barley</p>
        </a>
        <nav class="header__nav">
            <ul>
                <li><a href="home.html">Products</a></li>
                <li><a href="guides-recipes.html">Guides & Recipes</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">Resources</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <div class="header__auth-buttons" id="auth-guest">
            <a href="login.html" class="button button--secondary">Sign in</a>
            <a href="register.html" class="button button--primary">Register</a>
        </div>
        <div class="header__user-actions" id="auth-user">
            <a href="account.html" class="user-icon" aria-label="My Account">
                <img src="../static/img/icons/User_alt.svg" alt="User Account">
            </a>
            <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
                <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
            </a>

        </div>
    </div>
</header>

<!-- Main Content -->
<main class="page-product">
    <div class="container">
        <!-- Product Info Section -->
        <section class="product-details-section">
            <div class="product-image-container">
                <img src="../static/img/products/saaz_hops.jpg" alt="Saaz Hops" class="product-image">
            </div>
            <div class="product-info-column">
                <div class="product-title-price">
                    <h1 class="product-name">Saaz Hops</h1>
                    <div class="price-section">
                        <span class="price-tag">per 100g</span>
                        <p class="product-price">$4.75</p>
                    </div>
                </div>
                <div class="product-description">
                    <p>Saaz is a noble hop, the heart and soul of classic Bohemian and Czech pilsners. Grown in the Žatec region of the Czech Republic, it possesses a delicate and refined aromatic profile that is unmistakable.</p>
                    <p>Its aroma is characterized by soft, spicy, herbal, and floral notes. Saaz is primarily used for aroma rather than bitterness, as its alpha acid content is low. It imparts a classic European elegance and clean taste to the beer.</p>
                    <p>If you aim to brew an authentic Czech pilsner, European lager, or Belgian ale, Saaz is an indispensable ingredient.</p>
                </div>
                <div class="cart-controls">
                    <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
                        <i class="fa-solid fa-cart-shopping"></i>
                        <span>Add to Cart</span>
                    </button>
                    <div class="quantity-counter is-hidden" id="quantity-counter">
                        <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
                        <span class="quantity-value">1 in cart</span>
                        <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
                    </div>
                </div>
            </div>
        </section>

        <!-- Technical Specifications Accordion -->
        <section class="accordion-section">
            <div class="accordion-item">
                <div class="accordion-title">
                    <h3>Technical Specifications</h3>
                    <i class="fa-solid fa-chevron-down accordion-icon"></i>
                </div>
                <div class="accordion-content">
                    <ul>
                        <li><strong>Origin:</strong> Czech Republic</li>
                        <li><strong>Type:</strong> Aroma</li>
                        <li><strong>Alpha Acids:</strong> 2.0% - 5.0%</li>
                        <li><strong>Beta Acids:</strong> 4.5% - 8.0%</li>
                        <li><strong>Aroma Profile:</strong> Mild, pleasant, earthy, spicy, and floral.</li>
                        <li><strong>Cohumulone:</strong> 23% - 28%</li>
                        <li><strong>Total Oil:</strong> 0.4 - 1.0 mL/100g</li>
                        <li><strong>Recommended Beer Styles:</strong> Bohemian Pilsner, German Pilsner, Light Lagers, Belgian Ales, Lambic</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Latest Reviews Section -->
        <section class="reviews-section">
            <h2 class="reviews-title">Latest reviews</h2>
            <div class="reviews-grid">
                <!-- Review Card 1 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">The Only Choice for Pilsners</h4>
                        <p class="review-text">Don't even think about brewing a Czech pilsner without Saaz. This hop *is* that flavor. Gentle, spicy, perfect. I always buy the fresh harvest; the aroma is just amazing.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar4.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">PilsnerPurist</span>
                    </div>
                </div>
                <!-- Review Card 2 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">Delicate and Refined</h4>
                        <p class="review-text">I used it in a Belgian Saison, and it added a wonderful, subtle complexity. It doesn't overpower the yeast character but complements it. Very pleased with the result.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar5.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">BelgianBrewer</span>
                    </div>
                </div>
                <!-- Review Card 3 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">Low Alpha, High Aroma</h4>
                        <p class="review-text">You need to know what you're buying this hop for. It provides almost no bitterness, so it's not suitable for that. But for late-boil aroma, it's unparalleled. Docking one star only because you need to use quite a bit for a noticeable effect.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar6.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">PracticalBrewer</span>
                    </div>
                </div>
            </div>
        </section>
    </div>
</main>

<!-- Footer -->
<footer>
    <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
    <nav class="footer__nav">
        <ul>
            <li><a href="#">Contact</a></li>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Community</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">License</a></li>
        </ul>
    </nav>
    <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-safale-us05-yeast.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SafAle US-05 Dry Ale Yeast | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head><body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="page-product">
  <div class="container">
    <!-- Product Info Section -->
    <section class="product-details-section">
      <div class="product-image-container">
        <img src="../static/img/products/safale_us05_yeast.jpg" alt="SafAle US-05 Dry Ale Yeast" class="product-image">
      </div>
      <div class="product-info-column">
        <div class="product-title-price">
          <h1 class="product-name">SafAle US-05 Dry Ale Yeast</h1>
          <div class="price-section">
            <span class="price-tag">per 11.5g sachet</span>
            <p class="product-price">$3.25</p>
          </div>
        </div>
        <div class="product-description">
          <p>SafAle US-05 is the most famous and popular American ale yeast in the world. This strain is renowned for its ability to produce clean, crisp beers with a neutral flavor profile, allowing the hop and malt character to shine through.</p>
          <p>With its high attenuation and high flocculation, US-05 is ideal for a wide range of American ale styles, from West Coast IPAs to American Pale Ales and Cream Ales. It forms a firm sediment, making racking and clarification easier.</p>
          <p>Reliable, easy to use, and available in a dry format, this yeast is the number one choice for brewers seeking consistent and predictable results.</p>
        </div>
        <div class="cart-controls">
          <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
            <i class="fa-solid fa-cart-shopping"></i>
            <span>Add to Cart</span>
          </button>
          <div class="quantity-counter is-hidden" id="quantity-counter">
            <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
            <span class="quantity-value">1 in cart</span>
            <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Technical Specifications Accordion -->
    <section class="accordion-section">
      <div class="accordion-item">
        <div class="accordion-title">
          <h3>Technical Specifications</h3>
          <i class="fa-solid fa-chevron-down accordion-icon"></i>
        </div>
        <div class="accordion-content">
          <ul>
            <li><strong>Origin:</strong> USA</li>
            <li><strong>Type:</strong> Dry Ale Yeast</li>
            <li><strong>Attenuation:</strong> 78-82%</li>
            <li><strong>Flocculation:</strong> Medium to High</li>
            <li><strong>Alcohol Tolerance:</strong> 9-11% ABV</li>
            <li><strong>Fermentation Temperature:</strong> 59-75°F (15-24°C)</li>
            <li><strong>Pitching Rate:</strong> 11.5g sachet for 5-6 gallons (20-23 L)</li>
            <li><strong>Recommended Beer Styles:</strong> American Pale Ale, American IPA, Brown Ale, Porter, Stout, American Wheat</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Latest Reviews Section -->
    <section class="reviews-section">
      <h2 class="reviews-title">Latest reviews</h2>
      <div class="reviews-grid">
        <!-- Review Card 1 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">The Workhorse of My Brewery</h4>
            <p class="review-text">I use US-05 for almost 80% of my ales. Incredibly reliable yeast. Always starts fast, ferments clean, and drops out nicely. You can't go wrong with this strain.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar5.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">Fermentation_Fred</span>
          </div>
        </div>
        <!-- Review Card 2 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Clean & Crisp, Perfect for IPAs</h4>
            <p class="review-text">If you want your hops to be the star of your IPA, this is your yeast. No off-flavors, just pure, bright hop aroma. US-05 has never failed me.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar6.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">HopHead_Jessie</span>
          </div>
        </div>
        <!-- Review Card 3 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Great for Beginners</h4>
            <p class="review-text">When I was just starting to brew, this was the yeast recommended to me, and I have no regrets. It's very forgiving with temperature and handles many beginner mistakes. The beer always turns out great!</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar7.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">NewbieBrewer_Mark</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-unmalted-wheat.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unmalted Wheat | Hop & Barley</title>

    <!-- Google Fonts & Font Awesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Main CSS -->
    <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
    <div class="header-container">
        <a href="home.html" class="header__logo">
            <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
            <p class="logo-text">Hop & Barley</p>
        </a>
        <nav class="header__nav">
            <ul>
                <li><a href="home.html">Products</a></li>
                <li><a href="guides-recipes.html">Guides & Recipes</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">Resources</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <div class="header__auth-buttons" id="auth-guest">
            <a href="login.html" class="button button--secondary">Sign in</a>
            <a href="register.html" class="button button--primary">Register</a>
        </div>
        <div class="header__user-actions" id="auth-user">
            <a href="account.html" class="user-icon" aria-label="My Account">
                <img src="../static/img/icons/User_alt.svg" alt="User Account">
            </a>
            <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
                <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
            </a>

        </div>
    </div>
</header>

<!-- Main Content -->
<main class="page-product">
    <div class="container">
        <!-- Product Info Section -->
        <section class="product-details-section">
            <div class="product-image-container">
                <img src="../static/img/products/unmalted_wheat.jpg" alt="Unmalted Wheat" class="product-image">
            </div>
            <div class="product-info-column">
                <div class="product-title-price">
                    <h1 class="product-name">Unmalted Wheat</h1>
                    <div class="price-section">
                        <span class="price-tag">per 1 lb</span>
                        <p class="product-price">$1.80</p>
                    </div>
                </div>
                <div class="product-description">
                    <p>Unmalted wheat is the secret ingredient behind the classic hazy, refreshing character of Belgian Witbier. Unlike malted wheat, this is raw, unprocessed grain that imparts a unique texture and flavor to the beer.</p>
                    <p>Using unmalted wheat provides the beer with its characteristic light haze, a smooth, silky body, and a subtle, bready-grainy flavor that doesn't overpower the delicate notes of coriander and orange peel. The high protein content of this grain also contributes to a dense and persistent head.</p>
                    <p>This ingredient is a must-have for any brewer aiming to recreate an authentic Belgian Witbier or to add complexity and body to other styles, such as Lambics.</p>
                </div>
                <div class="cart-controls">
                    <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
                        <i class="fa-solid fa-cart-shopping"></i>
                        <span>Add to Cart</span>
                    </button>
                    <div class="quantity-counter is-hidden" id="quantity-counter">
                        <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
                        <span class="quantity-value">1 in cart</span>
                        <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
                    </div>
                </div>
            </div>
        </section>

        <!-- Technical Specifications Accordion -->
        <section class="accordion-section">
            <div class="accordion-item">
                <div class="accordion-title">
                    <h3>Technical Specifications</h3>
                    <i class="fa-solid fa-chevron-down accordion-icon"></i>
                </div>
                <div class="accordion-content">
                    <ul>
                        <li><strong>Origin:</strong> Belgium / USA</li>
                        <li><strong>Type:</strong> Unmalted Adjunct</li>
                        <li><strong>Color (°L):</strong> ~2.0 °L</li>
                        <li><strong>Moisture:</strong> 12% max</li>
                        <li><strong>Protein:</strong> High (contributes to haze and head retention)</li>
                        <li><strong>Flavor Profile:</strong> Neutral, subtle raw grain, bready</li>
                        <li><strong>Usage:</strong> Typically 30-50% of the grist for Witbiers. Requires a cereal mash or a mash with high diastatic power malts (like Pilsner or 6-Row).</li>
                        <li><strong>Recommended Beer Styles:</strong> Belgian Witbier, Lambic, Grand Cru, certain Saisons.</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Latest Reviews Section -->
        <section class="reviews-section">
            <h2 class="reviews-title">Latest reviews</h2>
            <div class="reviews-grid">
                <!-- Review Card 1 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">The Key to a True Wit</h4>
                        <p class="review-text">I tried brewing witbiers with malted wheat, and they were okay. But as soon as I added unmalted wheat, everything fell into place! That signature light haze, that smoothness. This is it!</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar2.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">BelgianBeerGeek</span>
                    </div>
                </div>
                <!-- Review Card 2 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">Don't Forget the Rice Hulls!</h4>
                        <p class="review-text">Great product, gives the beer a perfect body. A little tip: don't forget to add rice hulls to the mash! This wheat is very sticky and can completely clog your filter bed. With hulls, no problem at all.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar3.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">MashMaster_Pro</span>
                    </div>
                </div>
                <!-- Review Card 3 -->
                <div class="review-card">
                    <div class="review-rating">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i>
                    </div>
                    <div class="review-body">
                        <h4 class="review-heading">Great result, tricky to work with</h4>
                        <p class="review-text">The result exceeded expectations, the witbier turned out silky and delicious. But it's definitely trickier to work with than malt. You need a good mill and patience during sparging. But for an authentic taste, it's worth it.</p>
                    </div>
                    <div class="review-author">
                        <img src="../static/img/avatars/avatar4.svg" alt="User avatar" class="author-avatar">
                        <span class="author-name">PatientBrewer</span>
                    </div>
                </div>
            </div>
        </section>
    </div>
</main>

<!-- Footer -->
<footer>
    <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
    <nav class="footer__nav">
        <ul>
            <li><a href="#">Contact</a></li>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Community</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">License</a></li>
        </ul>
    </nav>
    <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/product-west-coast-ipa-kit.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>West Coast IPA - All-Grain Kit | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="home.html" class="header__logo">
      <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__auth-buttons" id="auth-guest">
      <a href="login.html" class="button button--secondary">Sign in</a>
      <a href="register.html" class="button button--primary">Register</a>
    </div>
    <div class="header__user-actions" id="auth-user">
      <a href="account.html" class="user-icon" aria-label="My Account">
        <img src="../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="page-product">
  <div class="container">
    <!-- Product Info Section -->
    <section class="product-details-section">
      <div class="product-image-container">
        <img src="../static/img/products/ipa_kit.jpg" alt="West Coast IPA - All-Grain Kit" class="product-image">
      </div>
      <div class="product-info-column">
        <div class="product-title-price">
          <h1 class="product-name">West Coast IPA - All-Grain Kit</h1>
          <div class="price-section">
            <span class="price-tag">for 5 Gallons</span>
            <p class="product-price">$60.00</p>
          </div>
        </div>
        <div class="product-description">
          <p>Brew a craft brewing classic with our "West Coast IPA - All-Grain Kit"! This kit contains all the necessary ingredients to create a bright, bitter, and incredibly aromatic IPA in the style of the US West Coast.</p>
          <p>We've selected the perfect combination of malts to achieve a clean, dry body that serves as an excellent base for a hop explosion. The kit includes a powerful combination of Centennial, Simcoe, and Columbus hops, which provide a burst of citrus, pine, and resinous notes characteristic of this style.</p>
          <p>This kit is your ticket to the world of true West Coast IPA. It comes with detailed step-by-step instructions to guide you through every stage, from mashing to bottling.</p>
        </div>
        <div class="cart-controls">
          <button class="button button--primary add-to-cart-button" id="add-to-cart-btn">
            <i class="fa-solid fa-cart-shopping"></i>
            <span>Add to Cart</span>
          </button>
          <div class="quantity-counter is-hidden" id="quantity-counter">
            <button class="quantity-btn" data-action="decrease" aria-label="Decrease quantity"><i class="fa-solid fa-minus"></i></button>
            <span class="quantity-value">1 in cart</span>
            <button class="quantity-btn" data-action="increase" aria-label="Increase quantity"><i class="fa-solid fa-plus"></i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Technical Specifications Accordion -->
    <section class="accordion-section">
      <div class="accordion-item">
        <div class="accordion-title">
          <h3>Kit Specifications</h3>
          <i class="fa-solid fa-chevron-down accordion-icon"></i>
        </div>
        <div class="accordion-content">
          <ul>
            <li><strong>Kit Type:</strong> All-Grain</li>
            <li><strong>Batch Size:</strong> 5 Gallons (19 Liters)</li>
            <li><strong>Estimated OG:</strong> 1.065</li>
            <li><strong>Estimated FG:</strong> 1.012</li>
            <li><strong>Estimated ABV:</strong> 6.9%</li>
            <li><strong>IBU:</strong> 65</li>
            <li><strong>Included Ingredients:</strong>
              <ul>
                <li>12 lbs Maris Otter Pale Malt</li>
                <li>1 lb Caramel Malt 40L</li>
                <li>0.5 lb Dextrin Malt</li>
                <li>1 oz Columbus Hops (60 min)</li>
                <li>1 oz Simcoe Hops (15 min)</li>
                <li>1 oz Centennial Hops (5 min)</li>
                <li>2 oz Centennial Hops (Dry Hop)</li>
                <li>1 pack SafAle US-05 Dry Ale Yeast</li>
                <li>Whirlfloc Tablet, Priming Sugar, Step-by-step Instructions</li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Latest Reviews Section -->
    <section class="reviews-section">
      <h2 class="reviews-title">Latest reviews</h2>
      <div class="reviews-grid">
        <!-- Review Card 1 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Authentic West Coast Flavor!</h4>
            <p class="review-text">This kit is the bomb! The beer turned out exactly how I love it: bitter, aromatic, with a powerful pine-citrus profile. The instructions are very clear. Will definitely buy again.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar9.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">IPA_Lover_82</span>
          </div>
        </div>
        <!-- Review Card 2 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Great Value and Quality</h4>
            <p class="review-text">Excellent value for money. All ingredients are fresh, the malt is well-milled, and the hops are aromatic. Ended up with 5 gallons of excellent IPA. Much easier than sourcing everything separately.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar10.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">FrugalBrewer</span>
          </div>
        </div>
        <!-- Review Card 3 -->
        <div class="review-card">
          <div class="review-rating">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i>
          </div>
          <div class="review-body">
            <h4 class="review-heading">Awesome, but bitter!</h4>
            <p class="review-text">The kit is super, but be prepared for the bitterness! This is a real West Coast IPA, not a modern "smoothie". If you love the classics, you'll enjoy it. I might reduce the 60-minute hop addition slightly, but that's a matter of taste.</p>
          </div>
          <div class="review-author">
            <img src="../static/img/avatars/avatar1.svg" alt="User avatar" class="author-avatar">
            <span class="author-name">SweetToothHomebrew</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</main>

<!-- Footer -->
<footer>
  <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
  <nav class="footer__nav">
    <ul>
      <li><a href="#">Contact</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Resources</a></li>
      <li><a href="#">License</a></li>
    </ul>
  </nav>
  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- JS -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/register.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register | Hop & Barley</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

    <!-- Font Awesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Link to your main CSS file -->
    <link rel="stylesheet" href="../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
    <div class="header-container">
        <a href="home.html" class="header__logo">
            <img src="../static/img/logo.svg" alt="Hop & Barley Logo">
            <p class="logo-text">Hop & Barley</p>
        </a>
        <nav class="header__nav">
            <ul>
                <li><a href="home.html">Products</a></li>
                <li><a href="guides-recipes.html">Guides & Recipes</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">Resources</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>

        <!-- Block for unauthorized user -->
        <div class="header__auth-buttons" id="auth-guest">
            <a href="login.html" class="button button--secondary">Sign in</a>
            <a href="register.html" class="button button--primary">Register</a>
        </div>

        <!-- Block for authorized user -->
        <div class="header__user-actions" id="auth-user">
            <a href="account.html" class="user-icon" aria-label="My Account">
                <img src="../static/img/icons/User_alt.svg" alt="User Account">
            </a>
            <a href="cart.html" class="cart-icon" aria-label="Shopping Cart">
                <img src="../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
            </a>

        </div>
    </div>
</header>

<!-- Main Content -->
<main class="auth-page-wrapper">
    <div class="auth-background">
        <img src="../static/img/background/pattern.jpg" alt="Background pattern">
    </div>
    <div class="auth-form-container">
        <div class="auth-container auth-container--register">
            <div class="Legend">
                <h1 class="auth-title">Register</h1>
            </div>

            <form class="auth-form" id="register-form">
                <div class="InputField">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" class="Input" placeholder="Value" required>
                </div>
                <div class="InputField">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" class="Input" placeholder="Value" required>
                </div>

                <div class="CheckboxField">
                    <label class="checkbox-container">Remember me
                        <input type="checkbox" checked>
                        <span class="checkmark"></span>
                    </label>
                </div>

                <div class="ButtonGroup">
                    <button type="submit" class="button button--primary">Register</button>
                </div>
            </form>

            <p class="auth-switch">Already have an account? <a href="login.html">Sign in</a></p>
        </div>
    </div>
</main>

<!-- Footer -->
<footer>
    <img src="../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">
    <nav class="footer__nav">
        <ul>
            <li><a href="#">Contact</a></li>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Community</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">License</a></li>
        </ul>
    </nav>
    <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>
</footer>

<!-- Link to your main JavaScript file -->
<script src="../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/admin/add.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Add/Edit Product | Hop & Barley</title>

    <!-- Google Fonts & Font Awesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Main CSS -->
    <link rel="stylesheet" href="../../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
    <div class="header-container">
        <a href="../home.html" class="header__logo">
            <img src="../../static/img/logo.svg" alt="Hop & Barley Logo">
            <p class="logo-text">Hop & Barley</p>
        </a>
        <nav class="header__nav">
            <ul>
                <li><a href="../home.html">Products</a></li>
                <li><a href="guides-recipes.html">Guides & Recipes</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">Resources</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <div class="header__user-actions">
            <a href="../account.html" class="user-icon" aria-label="My Account">
                <img src="../../static/img/icons/User_alt.svg" alt="User Account">
            </a>
            <a href="../cart.html" class="cart-icon" aria-label="Shopping Cart">
                <img src="../../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
            </a>

        </div>
    </div>
</header>

<!-- Main Content -->
<main class="admin-page-wrapper">
    <div class="admin-container">
        <!-- Tabs Navigation -->
        <div class="admin-tabs">
            <a href="products.html" class="admin-tab active">Product Management</a>
            <a href="dashboard.html" class="admin-tab">Dashboard</a>
        </div>

        <!-- Content Area -->
        <div class="admin-content">
            <h1 class="admin-content__title">Admin - Product Stock</h1>

            <div class="admin-form-layout">
                <div class="admin-form-col-left">
                    <h2 class="admin-form-section-title">Control</h2>
                    <div class="image-upload-card">
                        <div class="image-upload-placeholder">
                            <i class="fa-regular fa-image"></i>
                        </div>
                        <input type="file" id="image-upload-input" class="is-hidden" accept="image/*">
                        <button type="button" class="button button--primary upload-btn" id="upload-image-btn">Upload Image</button>
                    </div>
                </div>

                <div class="admin-form-col-right">
                    <h2 class="admin-form-section-title">Information</h2>
                    <form id="product-form" class="product-info-form">
                        <div class="checkout-form-group">
                            <label for="prod-title">Title</label>
                            <input type="text" id="prod-title" class="Input" placeholder="Value">
                        </div>
                        <div class="checkout-form-group">
                            <label for="prod-description">description</label>
                            <textarea id="prod-description" class="Textarea" placeholder="Value" rows="4"></textarea>
                        </div>
                        <div class="checkout-form-group">
                            <label for="prod-price">price</label>
                            <input type="text" id="prod-price" class="Input" placeholder="Value">
                        </div>
                        <div class="checkout-form-group">
                            <label>category</label>
                            <div class="category-tags">
                                <button type="button" class="category-tag active">Label</button>
                                <button type="button" class="category-tag">Label</button>
                                <button type="button" class="category-tag">Label</button>
                                <button type="button" class="category-tag">Label</button>
                            </div>
                        </div>
                    </form>
                </div>

                <!-- Control buttons -->
                <div class="admin-form-actions">
                    <button type="submit" form="product-form" class="button button--primary">Save</button>
                    <button type="button" class="button button--secondary">Hide</button>
                    <button type="button" class="button button--danger">Delete</button>
                </div>
            </div>
        </div>
    </div>
</main>


<!--<footer>-->
<!--    <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>-->
<!--</footer>-->

<!-- JS -->
<script src="../../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/admin/dashboard.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin - Dashboard | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="../home.html" class="header__logo">
      <img src="../../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="../home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__user-actions">
      <a href="../account.html" class="user-icon" aria-label="My Account">
        <img src="../../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="../cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="admin-page-wrapper">
  <div class="admin-container">
    <!-- Tabs Navigation -->
    <div class="admin-tabs">
      <a href="products.html" class="admin-tab">Product Management</a>
      <a href="dashboard.html" class="admin-tab active">Dashboard</a>
    </div>

    <!-- Content Area -->
    <div class="admin-content">
      <h1 class="admin-content__title">Admin - Dashboard</h1>

      <!-- Filter Tags -->
      <div class="category-tags">
        <button type="button" class="category-tag active">Label</button>
        <button type="button" class="category-tag">Label</button>
        <button type="button" class="category-tag">Label</button>
        <button type="button" class="category-tag">Label</button>
      </div>

      <!-- Stats Cards Grid -->
      <div class="stats-grid">
        <!-- Card 1: Total Sales -->
        <div class="stat-card">
          <div class="stat-card__header">
            <span class="stat-card__title">Total Sales</span>
            <div class="stat-card__icon-wrapper" style="background-color: #e0f8e3;">
              <i class="fa-solid fa-arrow-trend-up" style="color: #34c759;"></i>
            </div>
          </div>
          <p class="stat-card__value">$89,000</p>
          <div class="stat-card__delta delta--down">
            <i class="fa-solid fa-arrow-down"></i>
            <span>4.3% Down from yesterday</span>
          </div>
        </div>
        <!-- Card 2: Total User -->
        <div class="stat-card">
          <div class="stat-card__header">
            <span class="stat-card__title">Total User</span>
            <div class="stat-card__icon-wrapper" style="background-color: #e6e5ff;">
              <i class="fa-solid fa-users" style="color: #5856d6;"></i>
            </div>
          </div>
          <p class="stat-card__value">40,689</p>
          <div class="stat-card__delta delta--up">
            <i class="fa-solid fa-arrow-up"></i>
            <span>8.5% Up from yesterday</span>
          </div>
        </div>
        <!-- Card 3: Total Order -->
        <div class="stat-card">
          <div class="stat-card__header">
            <span class="stat-card__title">Total Order</span>
            <div class="stat-card__icon-wrapper" style="background-color: #fff0d4;">
              <i class="fa-solid fa-box-archive" style="color: #ff9f0a;"></i>
            </div>
          </div>
          <p class="stat-card__value">10293</p>
          <div class="stat-card__delta delta--up">
            <i class="fa-solid fa-arrow-up"></i>
            <span>1.3% Up from past week</span>
          </div>
        </div>
        <!-- Card 4: Total Pending -->
        <div class="stat-card">
          <div class="stat-card__header">
            <span class="stat-card__title">Total Pending</span>
            <div class="stat-card__icon-wrapper" style="background-color: #ffe6e0;">
              <i class="fa-solid fa-clock-rotate-left" style="color: #ff3b30;"></i>
            </div>
          </div>
          <p class="stat-card__value">2040</p>
          <div class="stat-card__delta delta--up">
            <i class="fa-solid fa-arrow-up"></i>
            <span>1.8% Up from yesterday</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</main>

<!-- Footer -->
<!--<footer>-->
<!--  <img src="../../static/img/background/image-footer.svg" alt="Hop & Barley Hops Logo" class="footer__hops-logo">-->
<!--  <nav class="footer__nav">-->
<!--    <ul>-->
<!--      <li><a href="#">Contact</a></li>-->
<!--      <li><a href="#">FAQ</a></li>-->
<!--      <li><a href="#">Community</a></li>-->
<!--      <li><a href="#">Resources</a></li>-->
<!--      <li><a href="#">License</a></li>-->
<!--    </ul>-->
<!--  </nav>-->
<!--  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>-->
<!--</footer>-->

<!-- JS -->
<script src="../../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/templates/admin/products.html
--------------------

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin - Product Stock | Hop & Barley</title>

  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Main CSS -->
  <link rel="stylesheet" href="../../static/css/main.css">
</head>
<body>
<!-- Header -->
<header>
  <div class="header-container">
    <a href="../home.html" class="header__logo">
      <img src="../../static/img/logo.svg" alt="Hop & Barley Logo">
      <p class="logo-text">Hop & Barley</p>
    </a>
    <nav class="header__nav">
      <ul>
        <li><a href="../home.html">Products</a></li>
        <li><a href="guides-recipes.html">Guides & Recipes</a></li>
        <li><a href="#">Community</a></li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <div class="header__user-actions">
      <a href="../account.html" class="user-icon" aria-label="My Account">
        <img src="../../static/img/icons/User_alt.svg" alt="User Account">
      </a>
      <a href="../cart.html" class="cart-icon" aria-label="Shopping Cart">
        <img src="../../static/img/icons/Shopping_bag.svg" alt="Shopping Cart">
      </a>

    </div>
  </div>
</header>

<!-- Main Content -->
<main class="admin-page-wrapper">
  <div class="admin-container">
    <!-- Tabs Navigation -->
    <div class="admin-tabs">
      <a href="products.html" class="admin-tab active">Product Management</a>
      <a href="dashboard.html" class="admin-tab">Dashboard</a>
    </div>

    <!-- Content Area -->
    <div class="admin-content">
      <h1 class="admin-content__title">Admin - Product Stock</h1>
      <div class="admin-actions">
        <a href="add.html" class="button button--primary">
          <i class="fa-solid fa-plus"></i>
          <span>Add Product</span>
        </a>
      </div>

      <div class="admin-table-wrapper">
        <table class="admin-table">
          <thead>
          <tr>
            <th>id</th>
            <th>name</th>
            <th>description</th>
            <th>price</th>
            <th>category</th>
            <th>created_at</th>
            <th>updated_at</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$100.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$90.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$140.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$120.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$20.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$20.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$20.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$20.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$20.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          <tr>
            <td>122033</td>
            <td>name</td>
            <td>description</td>
            <td>$20.00</td>
            <td>category</td>
            <td>YYYY-MM-DD</td>
            <td>YYYY-MM-DD</td>
            <td><a href="add.html" class="button button--edit">Edit</a></td>
          </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination -->
      <div class="account-pagination">
        <a href="#" class="pagination-link-account disabled">← Previous</a>
        <a href="#" class="pagination-link-account">Next →</a>
      </div>
    </div>
  </div>
</main>

<!-- Footer -->
<!--<footer>-->
<!--  <p class="footer__copyright">© Hop & Barley 2025. All rights reserved</p>-->
<!--</footer>-->

<!-- JS -->
<script src="../../static/js/main.js"></script>
</body>
</html>

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/static/js/main.js
--------------------

document.addEventListener('DOMContentLoaded', function() {

    // --- General logic for all pages (Login/Logout Simulation) ---
    const loginForm = document.getElementById('login-form');
    const logoutButton = document.getElementById('logout-button');
    function checkLoginStatus() {
        if (localStorage.getItem('isLoggedIn') === 'true') {
            document.body.classList.add('user-logged-in');
        } else {
            document.body.classList.remove('user-logged-in');
        }
    }
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            localStorage.setItem('isLoggedIn', 'true');
            const nextUrl = new URLSearchParams(window.location.search).get('next');
            window.location.href = nextUrl || 'home.html';
        });
    }
    if (logoutButton) {
        logoutButton.addEventListener('click', function(e) {
            e.preventDefault();
            localStorage.removeItem('isLoggedIn');
            window.location.href = 'home.html';
        });
    }
    checkLoginStatus();


    // --- Logic for the Main Page (home.html) ---
    const homePageContent = document.querySelector('.main-content-grid');
    if (homePageContent) {
        // 1. Sort Options Logic
        const sortButtons = document.querySelectorAll('.sort-options .sort-button');
        sortButtons.forEach(button => {
            button.addEventListener('click', function() {
                sortButtons.forEach(btn => btn.classList.remove('active-sort'));
                this.classList.add('active-sort');
            });
        });

        // 2. Pagination Logic
        const paginationList = document.querySelector('.pagination-list');
        if (paginationList) {
            const paginationLinks = paginationList.querySelectorAll('.pagination__link');
            paginationLinks.forEach(link => {
                link.addEventListener('click', function(event) {
                    event.preventDefault();
                    paginationLinks.forEach(lnk => lnk.classList.remove('active'));
                    this.classList.add('active');
                });
            });
        }

        // 3. Filter Logic (Keywords and Checkboxes)
        const keywordsList = document.querySelector('.keywords-list');
        const checkboxes = document.querySelectorAll('.checkbox-group input[type="checkbox"]');

        if (keywordsList && checkboxes.length > 0) {

            checkboxes.forEach(checkbox => {
                checkbox.addEventListener('change', function() {
                    const keyword = this.dataset.keyword;
                    if (this.checked) {
                        if (!document.querySelector(`.keyword-tag[data-keyword="${keyword}"]`)) {
                            const newTag = document.createElement('span');
                            newTag.className = 'keyword-tag';
                            newTag.setAttribute('data-keyword', keyword);
                            newTag.innerHTML = `${keyword} <i class="fa-solid fa-xmark remove-keyword-icon"></i>`;
                            keywordsList.appendChild(newTag);
                        }
                    } else {
                        const tagToRemove = document.querySelector(`.keyword-tag[data-keyword="${keyword}"]`);
                        if (tagToRemove) {
                            tagToRemove.remove();
                        }
                    }
                });
            });

            keywordsList.addEventListener('click', function(event) {
                const keywordIcon = event.target.closest('.remove-keyword-icon');
                if (keywordIcon) {
                    const keywordTag = keywordIcon.closest('.keyword-tag');
                    const keywordText = keywordTag.dataset.keyword;
                    const checkbox = document.querySelector(`.checkbox-container input[data-keyword="${keywordText}"]`);
                    if (checkbox) {
                        checkbox.checked = false;
                    }
                    keywordTag.remove();
                }
            });
        }
    }

    // --- Logic for Product Detail Pages (product-*.html) ---
    const productPageContent = document.querySelector('.page-product');
    if (productPageContent) {
        // Accordion
        const accordionTitle = document.querySelector('.accordion-title');
        if (accordionTitle) {
            accordionTitle.addEventListener('click', function() {
                this.closest('.accordion-item').classList.toggle('active');
            });
        }
        // "Add to Cart" Button and Counter
        const cartControls = document.querySelector('.cart-controls');
        if (cartControls) {
            const addToCartBtn = cartControls.querySelector('#add-to-cart-btn');
            const quantityCounter = cartControls.querySelector('#quantity-counter');
            const decreaseBtn = quantityCounter.querySelector('[data-action="decrease"]');
            const increaseBtn = quantityCounter.querySelector('[data-action="increase"]');
            const quantityValueSpan = quantityCounter.querySelector('.quantity-value');
            let quantity = 0;
            function updateView() {
                if (quantity === 0) {
                    addToCartBtn.classList.remove('is-hidden');
                    quantityCounter.classList.add('is-hidden');
                } else {
                    addToCartBtn.classList.add('is-hidden');
                    quantityCounter.classList.remove('is-hidden');
                    quantityValueSpan.textContent = `${quantity} in cart`;
                }
            }
            addToCartBtn.addEventListener('click', function() { quantity = 1; updateView(); });
            decreaseBtn.addEventListener('click', function() { if (quantity > 0) { quantity--; updateView(); } });
            increaseBtn.addEventListener('click', function() { quantity++; updateView(); });
            updateView();
        }
    }

    // --- Logic for Cart Page (cart.html) ---
    const cartPageContent = document.querySelector('.cart-page-wrapper');
    if (cartPageContent) {
        const cartItemsList = document.getElementById('cart-items-list');
        const cartTotalPriceElem = document.getElementById('cart-total-price');
        function updateCartTotal() {
            let total = 0;
            document.querySelectorAll('.cart-item').forEach(item => {
                const priceText = item.querySelector('[data-item-total-price]').textContent;
                if (priceText) {
                    total += parseFloat(priceText.replace('$', ''));
                }
            });
            if (cartTotalPriceElem) cartTotalPriceElem.textContent = `$${total.toFixed(2)}`;
        }
        if (cartItemsList) {
            cartItemsList.addEventListener('click', function(event) {
                const cartItem = event.target.closest('.cart-item');
                if (!cartItem) return;
                const quantityElem = cartItem.querySelector('.quantity-value-cart');
                const itemTotalElem = cartItem.querySelector('[data-item-total-price]');
                const basePrice = parseFloat(cartItem.dataset.price);
                let quantity = parseInt(quantityElem.textContent);
                if (event.target.closest('[data-action="increase"]')) {
                    quantity++;
                } else if (event.target.closest('[data-action="decrease"]')) {
                    quantity = quantity > 1 ? quantity - 1 : 0;
                }
                if (event.target.closest('[data-action="remove"]') || quantity === 0) {
                    cartItem.remove();
                } else {
                    quantityElem.textContent = quantity;
                    itemTotalElem.textContent = `$${(basePrice * quantity).toFixed(2)}`;
                }
                updateCartTotal();
            });
        }
        updateCartTotal();
    }

    // --- Logic for Account and Admin Pages ---
    const accountAdminWrapper = document.querySelector('.account-page-wrapper, .admin-page-wrapper');
    if (accountAdminWrapper) {
        // Account Page Tabs
        const accountTabs = document.querySelectorAll('.account-tab');
        const tabPanes = document.querySelectorAll('.tab-pane');
        if (accountTabs.length > 0 && tabPanes.length > 0) {
            accountTabs.forEach(tab => {
                tab.addEventListener('click', function() {
                    accountTabs.forEach(item => item.classList.remove('active'));
                    tabPanes.forEach(pane => pane.classList.remove('active'));
                    const targetPane = document.querySelector(this.dataset.tabTarget);
                    this.classList.add('active');
                    if (targetPane) targetPane.classList.add('active');
                });
            });
        }

        // Admin Panel - Category Tags
        const categoryTagsContainer = document.querySelector('.category-tags');
        if (categoryTagsContainer) {
            categoryTagsContainer.addEventListener('click', function(e) {
                const clickedTag = e.target.closest('.category-tag');
                if (clickedTag) {
                    categoryTagsContainer.querySelectorAll('.category-tag').forEach(t => t.classList.remove('active'));
                    clickedTag.classList.add('active');
                }
            });
        }

        // Image Upload Simulation
        const uploadButton = document.getElementById('upload-image-btn');
        const fileInput = document.getElementById('image-upload-input');

        if (uploadButton && fileInput) {
            uploadButton.addEventListener('click', function() {
                fileInput.click();
            });

            fileInput.addEventListener('change', function(event) {
                const file = event.target.files[0];
                if (file) {
                    const reader = new FileReader();
                    const placeholder = document.querySelector('.image-upload-placeholder');

                    reader.onload = function(e) {
                        placeholder.innerHTML = '';
                        placeholder.style.backgroundImage = `url('${e.target.result}')`;
                        placeholder.style.backgroundSize = 'cover';
                        placeholder.style.backgroundPosition = 'center';
                    }
                    reader.readAsDataURL(file);
                }
            });
        }
    }
});

--------------------
File: /Hop-and-Barley-main/Hop-and-Barley-main/myshop/static/css/main.css
--------------------

/* CSS Variables for Colors and Fonts */
:root {
    --black-main: #111d13;
    --grey-text: #757575;
    --border-default: #d9d9d9;
    --slate-200: #e3e3e3;
    --black-200: rgba(12, 12, 13, 0.1);
    --black-100: rgba(12, 12, 13, 0.05);
    --background-grey: #fff;
    --border-dark-grey: #767676;
    --white-text: #f5f5f5;
    --background-default: #f5f5f5;
    --background: #fff;
    --dark-green: #31572c;
    --green: #02542d;
    --background-green: #cff7d3;
    --background-header: #fff;

    --font-family: "Inter", sans-serif;
}

/* Base styles */
body {
    font-family: var(--font-family);
    color: var(--black-main);
    background-color: var(--background);
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

*, *::before, *::after {
    box-sizing: inherit;
}

a {
    text-decoration: none;
    color: inherit;
}

p, h1, h2, h3, h4, h5, h6 {
    margin: 0;
}

/* Container */
.container {
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 64px;
}

/* Header styles */
header {
    width: 100%;
    height: 100px;
    padding: 32px 64px;
    background-color: var(--background-header);
    border-bottom: 1px solid var(--border-default);
    display: flex;
    justify-content: center;
    align-items: center;
}

.header-container {
    width: 100%;
    max-width: 1312px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header__logo {
    display: flex;
    align-items: center;
    gap: 24px;
}

.header__logo img {
    width: 26px;
    height: 37.52px;
    border-radius: 8px;
}

.header__logo .logo-text {
    font-size: 24px;
    font-weight: 700;
    line-height: 1;
    color: var(--black-main);
}

.header__nav ul {
    width: 640px;
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header__nav a {
    padding: 8px;
    font-size: 16px;
    line-height: 1;
    color: var(--black-main);
    font-weight: 500;
    transition: color 0.2s ease;
}

.header__nav a:hover {
    color: var(--dark-green);
}

.header__auth-buttons {
    width: 192px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.button {
    flex: 1 1 0;
    padding: 8px;
    border-radius: 8px;
    font-size: 16px;
    line-height: 1;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
}

.button--secondary {
    background-color: var(--border-default);
    border: 1px solid var(--border-dark-grey);
    color: var(--black-main);
}

.button--secondary:hover {
    background-color: var(--slate-200);
}

.button--primary {
    background-color: var(--green);
    border: 1px solid var(--green);
    color: var(--white-text);
}

.button--primary:hover {
    background-color: var(--dark-green);
    border-color: var(--dark-green);
}

/* Hero Banner */
.hero-banner {
    position: relative;
    max-width: 1312px;
    margin: 0 auto 32px;
    height: 400px;
    overflow: hidden;
    padding: 0 64px;
}

/*.hero-banner {*/
/*    position: relative;*/
/*    width: 100%;*/
/*    height: 400px;*/
/*    overflow: hidden;*/
/*    margin-bottom: 32px;*/
/*}*/

.hero-banner__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
    border-radius: 8px;
}

.hero-banner__overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1000;
}

/* Main Content Grid */
.main-content-grid {
    display: grid;
    grid-template-columns: 304px 1fr;
    gap: 32px;
    align-items: flex-start;
    padding-bottom: 64px;
}

/* Sidebar */
.sidebar {
    padding: 16px;
    background-color: var(--background-default);
    border-radius: 8px;
    border: 1px solid var(--border-default);
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.sidebar__section {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.section-title {
    font-size: 16px;
    line-height: 1.4;
    color: var(--black-main);
}

.keywords-list {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
}

.keyword-tag {
    padding: 8px;
    background-color: var(--background-green);
    color: var(--green);
    border-radius: 8px;
    font-size: 16px;
    line-height: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.remove-keyword-icon {
    cursor: pointer;
    color: inherit;
    font-size: 12px;
}

/* Custom Checkboxes */
.checkbox-group {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.checkbox-container {
    display: block;
    position: relative;
    padding-left: 28px;
    cursor: pointer;
    font-size: 16px;
    line-height: 1.4;
    color: var(--black-main);
    user-select: none;
}

.checkbox-container input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
}

.checkmark {
    position: absolute;
    top: 2px;
    left: 0;
    height: 16px;
    width: 16px;
    background-color: var(--background-grey);
    border: 1px solid var(--border-default);
    border-radius: 4px;
    transition: background-color 0.2s ease, border-color 0.2s ease;
}

.checkbox-container input:checked ~ .checkmark {
    background-color: var(--green);
    border-color: var(--green);
}

.checkmark:after {
    font-family: "Font Awesome 6 Free";
    font-weight: 900;
    content: "\f00c";
    position: absolute;
    display: none;
    color: white;
    font-size: 10px;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

.checkbox-container input:checked ~ .checkmark:after {
    display: block;
}

/* Search & Sort Bar */
.search-sort-bar {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 48px;
}

.search-input-wrapper {
    flex: 1 1 0;
    max-width: 327px;
    position: relative;
}

.search-input {
    width: 100%;
    height: 40px;
    padding: 12px 40px 12px 16px;
    border: 1px solid var(--border-default);
    border-radius: 9999px;
    font-size: 16px;
    line-height: 1;
    color: var(--black-main);
    background-color: var(--background-default);
}

.search-input::placeholder {
    color: #b3b3b3;
}

.search-button {
    position: absolute;
    right: 16px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    cursor: pointer;
    color: var(--grey-text);
    font-size: 16px;
    padding: 0;
}

.sort-options {
    display: flex;
    gap: 8px;
}

.sort-button {
    padding: 8px;
    background-color: var(--background-grey);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    font-size: 16px;
    line-height: 1;
    color: var(--grey-text);
    display: flex;
    align-items: center;
    gap: 8px;
}

.sort-button.active-sort {
    background-color: var(--green);
    border-color: var(--green);
    color: var(--white-text);
}

/* Product Grid */
.product-grid {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
}

.product-card {
    padding: 16px;
    background-color: var(--background-default);
    border-radius: 8px;
    border: 1px solid var(--border-default);
    box-shadow: 0 2px 5px var(--black-100);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px var(--black-200);
}

.product-card__image {
    width: 100%;
    height: 247px;
    object-fit: cover;
    border-radius: 8px;
}

.product-card__info {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.product-card__name {
    font-size: 16px;
    line-height: 1.4;
    color: var(--black-main);
    font-weight: 600;
}

.product-card__price {
    font-size: 16px;
    font-weight: 600;
    line-height: 1.4;
    color: var(--black-main);
}

.product-card__description {
    font-size: 14px;
    line-height: 1.4;
    color: var(--grey-text);
}

/* Pagination */
.pagination {
    width: 100%;
    margin-top: 48px;
    background-color: var(--background-default);
    border-radius: 16px;
    border: 1px solid var(--border-default);
    padding: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.pagination-list {
    display: flex;
    gap: 8px;
    margin: 0 16px;
}

.pagination__link {
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 16px;
    line-height: 1;
    color: var(--black-main);
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.pagination__link--prev,
.pagination__link--next {
    color: var(--grey-text);
    opacity: 0.5;
}

.pagination__link--prev:hover,
.pagination__link--next:hover {
    opacity: 1;
    color: var(--black-main);
}

.pagination__link:hover:not(.active) {
    background-color: #e0e0e0;
}

.pagination__link.active {
    background-color: var(--black-main);
    color: var(--white-text);
}

.pagination__dots {
    font-size: 16px;
    font-weight: 700;
    line-height: 1.4;
    color: var(--black-main);
    padding: 8px 12px;
}

/* Footer */
footer {
    width: 100%;
    padding: 48px 64px 24px 64px;
    background-color: var(--black-main);
    color: var(--white-text);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 48px;
}

.footer__hops-logo {
    width: 483.92px;
    height: 263.53px;
}

.footer__nav {
    width: 640px;
    height: 37px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.footer__nav ul {
    width: 100%;
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.footer__nav a {
    font-size: 16px;
    line-height: 1;
    color: var(--white-text);
    padding: 8px;
    transition: opacity 0.2s ease;
}

.footer__nav a:hover {
    opacity: 0.8;
}

.footer__copyright {
    font-size: 14px;
    line-height: 20px;
    color: var(--white-text);
}

/* Link wrapper for product cards */
.product-card-link {
    text-decoration: none;
}


/*
========================================
    Register Page Specific Styles
========================================
*/
.auth-page-wrapper {
    position: relative;
    width: 100%;
    height: 757px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

.auth-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
}

.auth-background img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}



.auth-form-container {
    position: relative;
    z-index: 2;
}

.auth-container--register {
    width: 416px;
    height: auto;
    padding: 24px;
    background: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 24px;
}

.Legend {
    width: 100%;
    align-self: stretch;
}

.auth-title {
    font-size: 24px;
    font-weight: 600;
    line-height: 1.2;
    color: var(--black-main);
}

.auth-form {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.InputField {
    width: 100%; /* 368px */
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.InputField label {
    font-size: 16px;
    line-height: 1.4;
    color: var(--black-main);
    font-weight: 500;
}

.Input {
    width: 100%;
    height: 40px;
    padding: 12px 16px;
    background-color: var(--background-grey);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    font-size: 16px;
    line-height: 1;
    color: var(--black-main);
}

.Input:focus {
    outline: none;
    border-color: var(--green);
    box-shadow: 0 0 0 3px rgba(2, 84, 45, 0.2);
}


.CheckboxField {
    width: 100%;
}

.CheckboxField .checkbox-container {
    margin-bottom: 0;
    font-size: 16px;
    line-height: 1;
    color: var(--black-main);
}

/* ButtonGroup  */
.ButtonGroup {
    width: 100%;
}

.ButtonGroup .button {
    width: 100%;
    height: 40px;
    padding: 12px;
}

/* auth-switch - link "Already have an account?" */
.auth-switch {
    margin-top: 0;
    font-size: 14px;
    color: var(--grey-text);
}


/*
========================================
    Login Page Specific Styles
========================================
*/

.auth-container--login {
    width: 416px;
    padding: 24px;
    background: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 24px;
}

.auth-container--login .auth-form {
    gap: 24px;
}

/* Forgot password  */
.TextLink {
    width: 100%;
    text-align: left;
}

.TextLink a {
    font-size: 14px;
    font-weight: 500;
    color: var(--green);
    text-decoration: none;
    transition: text-decoration 0.2s ease;
}

.TextLink a:hover {
    text-decoration: underline;
}


/*
========================================
    Forgot Password Page Specific Styles
========================================
*/
.auth-container--forgot-password {
    width: 416px;
    padding: 24px;
    background: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
}

.auth-container--forgot-password .auth-form {
    gap: 24px;
}

.ButtonGroup--center {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 16px;
}

.ButtonGroup--center .button {
    flex: 1 1 0;
    padding: 12px;
    height: 40px;
}

/* Button - "Cancel" */
.button--cancel {
    background-color: transparent;
    color: var(--black-main);
    font-weight: 500;
    border: 1px solid var(--border-dark-grey);
}

.button--cancel:hover {
    background-color: var(--slate-200);
}


/*
========================================
    Header User Actions (Logged-in state)
========================================
*/
.header__user-actions {
    display: none;
    align-items: center;
    gap: 24px;
}

.user-icon, .cart-icon {
    display: block;
    width: 38px;
    height: 38px;
}

.user-icon img, .cart-icon img {
    width: 100%;
    height: 100%;
}

.button--logout {
    background-color: transparent;
    border: 1px solid var(--border-dark-grey);
    color: var(--black-main);
    padding: 8px 16px;
}

/*
========================================
    Logic for Hiding/Showing Auth Blocks
========================================
*/

body:not(.user-logged-in) .header__user-actions {
    display: none;
}
body:not(.user-logged-in) .header__auth-buttons {
    display: flex;
}

body.user-logged-in .header__auth-buttons {
    display: none;
}
body.user-logged-in .header__user-actions {
    display: flex;
}


/*
========================================
    Product Detail Page Styles
========================================
*/
.page-product {
    background-color: var(--background-grey);
    padding: 64px 0;
}

.page-product .container > section {
    margin-bottom: 64px;
}
.page-product .container > section:last-child {
    margin-bottom: 0;
}

/* --- Product Details Section --- */
.product-details-section {
    display: flex;
    gap: 32px;
}

.product-image-container {
    width: 640px;
    height: 484px;
    flex-shrink: 0;
}

.product-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 8px;
}

.product-info-column {
    display: flex;
    flex-direction: column;
    gap: 24px;
    flex-grow: 1;
}

.product-title-price {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.product-name {
    font-size: 24px;
    font-weight: 600;
    line-height: 1.2;
    color: var(--black-main);
}

.price-section {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.price-tag {
    font-size: 16px;
    line-height: 1;
    color: var(--green);
    background-color: var(--background-green);
    padding: 8px;
    border-radius: 8px;
    align-self: flex-start;
}

.product-price {
    font-size: 48px;
    font-weight: 600;
    line-height: 1.4;
    color: var(--black-main);
}

.product-description {
    font-size: 16px;
    line-height: 1.4;
    color: var(--black-main);
    display: flex;
    flex-direction: column;
    gap: 1em;
}

/*  Add to Cart" Button  */
.add-to-cart-button {
    width: 304px;
    height: 40px;
    padding: 12px;
    gap: 8px;
}

.add-to-cart-button .fa-check {
    display: none;
}
.add-to-cart-button.is-added {
    background-color: var(--dark-green);
    cursor: default;
}
.add-to-cart-button.is-added .fa-cart-shopping {
    display: none;
}
.add-to-cart-button.is-added .fa-check {
    display: inline-block;
}

/* --- Accordion Section  --- */
.accordion-section {
}

.accordion-item {
    width: 640px;
    background-color: white;
    border: 1px solid var(--border-default);
    border-radius: 8px;
    padding: 24px;
}

.accordion-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    width: 100%;
}

.accordion-title h3 {
    font-size: 24px;
    font-weight: 600;
    line-height: 1.4;
    color: #1e1e1e;
}

.accordion-icon {
    transition: transform 0.3s ease;
}

.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease, padding-top 0.3s ease;
}
.accordion-content ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.accordion-content li {
    font-size: 16px;
    line-height: 1.4;
}

.accordion-item.active .accordion-content {
    max-height: 500px;
    padding-top: 16px;
}
.accordion-item.active .accordion-icon {
    transform: rotate(180deg);
}

/* --- Reviews Section --- */
.reviews-section {
    display: flex;
    flex-direction: column;
    gap: 48px;
}

.reviews-title {
    font-size: 24px;
    font-weight: 600;
    line-height: 1.2;
    color: var(--black-main);
}

.reviews-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 32px;
}

.review-card {
    padding: 24px;
    background-color: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.review-rating {
    display: flex;
    gap: 4px;
    color: #FFC107;
    font-size: 20px;
}

.review-body {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.review-heading {
    font-size: 24px;
    font-weight: 600;
    line-height: 1.2;
    color: #1e1e1e;
}

.review-text {
    font-size: 16px;
    line-height: 1.4;
    color: #1e1e1e;
}

.review-author {
    display: flex;
    align-items: center;
    gap: 12px;
}

.author-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
}

.author-name {
    font-size: 16px;
    font-weight: 600;
    line-height: 1.4;
    color: var(--grey-text);
}

/*
========================================
    Cart Controls & Quantity Counter
========================================
*/
.cart-controls {
    width: 304px;
    height: 40px;
}

.is-hidden {
    display: none !important;
}

.quantity-counter {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    height: 100%;
    background-color: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    padding: 0 12px;
}

.quantity-btn {
    background-color: transparent;
    border: none;
    cursor: pointer;
    width: 24px;
    height: 24px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    color: var(--black-main);
    transition: background-color 0.2s ease;
}

.quantity-btn:hover {
    background-color: var(--slate-200);
}

.quantity-value {
    font-size: 16px;
    font-weight: 600;
    color: var(--dark-green);
}

/*
========================================
    Shopping Cart Page Styles
========================================
*/
.cart-page-wrapper {
    background-color: var(--background-grey);
    padding: 64px 0;
}

.cart-container {
    max-width: 640px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 48px;
}

.cart-title {
    font-size: 24px;
    font-weight: 600;
    line-height: 1.2;
    color: var(--black-main);
}

.cart-items-list {
    display: flex;
    flex-direction: column;
    gap: 48px;
}

.cart-item {
    padding: 24px;
    background-color: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    gap: 24px;
}

.cart-item__image {
    width: 160px;
    height: 160px;
    object-fit: cover;
    border-radius: 8px;
    flex-shrink: 0;
}

.cart-item__body {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 24px;
}

.cart-item__details {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.cart-item__name {
    font-size: 24px;
    font-weight: 600;
    line-height: 1.2;
}

.cart-item__price-info {
    display: flex;
    align-items: center;
    gap: 16px;
}

.cart-item__price {
    font-size: 31px;
    font-weight: 600;
    line-height: 1.4;
}

.cart-item__price-tag {
    font-size: 16px;
    line-height: 1;
    color: var(--green);
    background-color: var(--background-green);
    padding: 8px;
    border-radius: 8px;
}

.cart-item__actions {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.cart-item__quantity-selector {
    width: 102px;
    height: 40px;
    padding: 12px;
    background-color: var(--background-grey);
    border: 1px solid var(--border-dark-grey);
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.quantity-btn-cart {
    background: none;
    border: none;
    cursor: pointer;
    color: var(--black-main);
    padding: 0;
}

.quantity-value-cart {
    font-size: 16px;
    font-weight: 500;
}

.button--remove {
    background-color: var(--background-grey);
    border: 1px solid var(--border-dark-grey);
    border-radius: 8px;
    padding: 12px;
    font-size: 16px;
    color: var(--black-main);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: background-color 0.2s ease, color 0.2s ease;
}

.button--remove:hover {
    background-color: #fbebeb;
    color: #c81e1e;
}

/* Cart Summary */
.cart-summary {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.cart-summary__total {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 10px;
}

.cart-summary__total p {
    font-size: 20px;
    font-weight: 700;
}

.button--checkout {
    width: 100%;
    height: 40px;
    padding: 12px;
}

/*
========================================
    Checkout Page Styles
========================================
*/
.checkout-page-wrapper {
    background-color: var(--background-grey);
    padding: 64px 0;
}

.checkout-container {
    max-width: 640px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 48px;
}

.checkout-title {
    color: var(--black-main);
    font-size: 24px;
    font-weight: 600;
    line-height: 1.2;
}

#checkout-form {
    display: flex;
    flex-direction: column;
    gap: 48px;
}

.checkout-section {
    width: 100%;
    padding: 24px;
    background-color: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.checkout-section__title {
    font-size: 24px;
    font-weight: 600;
    line-height: 1.2;
    color: var(--black-main);
}

.checkout-form-group {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.checkout-form-group label {
    font-size: 16px;
    line-height: 1.4;
    color: var(--black-main);
    font-weight: 500;
}

.Textarea {
    width: 100%;
    padding: 12px 16px;
    background-color: var(--background-grey);
    border-radius: 8px;
    border: 1px solid var(--border-default);
    font-size: 16px;
    font-family: inherit;
    line-height: 1.4;
    resize: vertical;
}

/* Payment Method Radio Buttons */
.payment-options {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.radio-option {
    width: 100%;
    height: 46px;
    padding: 12px 16px;
    background-color: var(--background-grey);
    border-radius: 8px;
    border: 1px solid var(--border-default);
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: 12px;
}

.radio-option input[type="radio"] {
    display: none;
}

.radio-custom {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    border: 1px solid var(--grey-text);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-shrink: 0;
    transition: border-color 0.2s ease;
}

.radio-custom::after {
    content: '';
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: var(--black-main);
    display: block;
    transform: scale(0);
    transition: transform 0.2s ease;
}

.radio-option input[type="radio"]:checked + .radio-custom {
    border-color: var(--black-main);
}

.radio-option input[type="radio"]:checked + .radio-custom::after {
    transform: scale(1);
}

.radio-label {
    font-size: 16px;
    line-height: 1.4;
    color: #1e1e1e;
}

/* Order Summary */
.checkout-summary {
    background-color: var(--background-green);
    padding: 24px;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.summary-details {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.summary-total {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 10px;
}

.summary-total p {
    font-size: 20px;
    font-weight: 700;
}

.button--pay {
    width: 100%;
    height: 40px;
    padding: 12px;
}

/*
========================================
    Account Page Styles
========================================
*/
.account-page-wrapper {
    background-color: var(--background-grey);
    padding: 64px 0;
}

.account-container {
    max-width: 640px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 32px;
}

/* Tabs Navigation */
.account-tabs {
    display: flex;
    border-bottom: 1px solid var(--border-default);
}

.account-tab {
    padding: 4px 12px;
    font-size: 16px;
    line-height: 1.4;
    border: none;
    background-color: transparent;
    cursor: pointer;
    color: var(--grey-text);
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
    transition: color 0.2s ease, border-color 0.2s ease;
}

.account-tab:hover {
    color: var(--black-main);
}

.account-tab.active {
    color: var(--black-main);
    font-weight: 600;
    border-bottom-color: var(--black-main);
}

/* Tabs Content */
.tab-pane {
    display: none;
}

.tab-pane.active {
    display: block;
}

/* Order History Table */
.order-history-table {
    width: 100%;
    background-color: var(--background-default);
    border-radius: 16px;
    border: 1px solid var(--border-default);
    overflow: hidden; /* To clip corners of header */
}

.order-table-header {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr; /* 3-column layout */
    background-color: var(--background-green);
    font-weight: 700;
}

.order-table-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    border-top: 1px solid var(--border-default);
}

.order-table-cell {
    padding: 20px;
    font-size: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.order-date {
    color: var(--grey-text);
}

/* Pagination for Account Page */
.account-pagination {
    margin-top: 24px;
    padding: 24px;
    background-color: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.pagination-link-account {
    font-size: 16px;
    color: var(--black-main);
    font-weight: 500;
}

.pagination-link-account.disabled {
    color: var(--grey-text);
    opacity: 0.5;
    pointer-events: none;
}


/*
========================================
    Account Information Form Styles
========================================
*/
.account-form-container {
    padding: 24px;
    background-color: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.account-form-title {
    font-size: 24px;
    font-weight: 700;
    line-height: 1;
    color: var(--black-main);
}

#account-info-form {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

/* button "Save"*/
.button--full-width {
    width: 100%;
    height: 40px;
    padding: 12px;
}


/*
========================================
    Admin Panel Styles
========================================
*/
.admin-page-wrapper {
    background-color: var(--background-grey);
    padding: 64px;
}

.admin-container {
    max-width: 1312px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 32px;
}

/* Tabs Navigation */
.admin-tabs {
    display: flex;
    border-bottom: 1px solid var(--border-default);
}

.admin-tab {
    padding: 4px 12px;
    font-size: 16px;
    line-height: 1.4;
    border: none;
    background-color: transparent;
    cursor: pointer;
    color: var(--grey-text);
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
    transition: color 0.2s ease, border-color 0.2s ease;
}

.admin-tab:hover {
    color: var(--black-main);
}

.admin-tab.active {
    color: var(--black-main);
    font-weight: 600;
    border-bottom-color: var(--black-main);
}

/* Admin Content */
.admin-content {
    display: flex;
    flex-direction: column;
    gap: 32px;
}

.admin-content__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.admin-content__title {
    font-size: 24px;
    font-weight: 600;
    line-height: 1.2;
    color: var(--black-main);
}

.admin-content__header .button {
    height: 40px;
    padding: 12px;
    gap: 8px;
}

/* Admin Table */
.admin-table-wrapper {
    width: 100%;
    border: 1px solid var(--border-default);
    border-radius: 16px;
    overflow: hidden;
}

.admin-table {
    width: 100%;
    border-collapse: collapse;
}

.admin-table th,
.admin-table td {
    padding: 20px;
    text-align: left;
    font-size: 16px;
    border-bottom: 1px solid var(--border-default);
}

.admin-table tr:last-child td {
    border-bottom: none;
}

.admin-table thead {
    background-color: var(--background-green);
}

.admin-table th {
    font-weight: 700;
    color: var(--black-main);
}

.admin-table td {
    color: var(--black-main);
    vertical-align: middle;
}

.button--edit {
    height: 36px;
    padding: 8px 16px;
    background-color: var(--green);
    color: var(--white-text);
    text-decoration: none;
    border-radius: 8px;
}

/*
========================================
    Admin Add/Edit Product Page Styles
========================================
*/
.admin-form-layout {
    display: grid;
    grid-template-columns: 208px 1fr;
    grid-template-rows: auto auto;
    gap: 32px 48px;
    width: 100%;
}

/* Левая колонка */
.admin-form-col-left {
    grid-column: 1 / 2;
    grid-row: 1 / 2;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

/* Правая колонка */
.admin-form-col-right {
    grid-column: 2 / 3;
    grid-row: 1 / 2;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

/* Кнопки внизу */
.admin-form-actions {
    grid-column: 2 / 3;
    grid-row: 2 / 3;
    display: flex;
    gap: 16px;
}

.admin-form-section-title {
    font-size: 20px;
    font-weight: 600;
}

/* Карточка загрузки изображения */
.image-upload-card {
    width: 208px;
    height: 272px;
    padding: 24px;
    background-color: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
}

.image-upload-placeholder {
    width: 100%;
    flex-grow: 1;
    margin-bottom: 24px;
    background-color: var(--slate-200);
    border-radius: 4px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--grey-text);
    font-size: 48px;
}

.upload-btn {
    width: 160px;
    height: 40px;
}

.product-info-form {
    padding: 24px;
    background-color: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    width: 100%;
}

/* Сategory */
.category-tags {
    display: flex;
    gap: 8px;
}

.category-tag {
    padding: 8px;
    border-radius: 8px;
    border: 1px solid var(--border-default);
    background-color: var(--slate-200);
    color: var(--grey-text);
    font-size: 14px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
}

.category-tag .fa-check {
    display: none;
}

.category-tag.active {
    background-color: var(--black-main);
    color: var(--white-text);
    border-color: var(--black-main);
}

.category-tag.active .fa-check {
    display: inline-block;
}

/* Save, Hide, Delete */
.admin-form-actions .button {
    height: 40px;
    padding: 12px 24px;
}

.button--danger {
    background-color: #dc3545;
    color: white;
    border: 1px solid #dc3545;
}

.button--danger:hover {
    background-color: #c82333;
    border-color: #bd2130;
}

/*
========================================
    Admin Dashboard Page Styles
========================================
*/
.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 32px;
}

.stat-card {
    padding: 24px;
    background-color: var(--background-default);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.stat-card__header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.stat-card__title {
    font-size: 16px;
    font-weight: 600;
    color: var(--black-main);
    opacity: 0.7;
}

.stat-card__icon-wrapper {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
}

.stat-card__value {
    font-size: 28px;
    font-weight: 700;
    color: var(--black-main);
}

.stat-card__delta {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 16px;
    font-weight: 500;
}

.delta--up {
    color: #34c759;
}

.delta--down {
    color: #ff3b30;
}

/*
========================================
    Static Content Page Styles
========================================
*/
.static-page-wrapper {
    background-color: var(--background-grey);
    padding: 80px 0;
    min-height: 60vh; /* Минимальная высота, чтобы футер не прилипал к хедеру */
    display: flex;
    align-items: center;
}

.static-page-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
    background-color: white;
    padding: 60px;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.static-page-title {
    font-size: 48px;
    font-weight: 700;
    color: var(--black-main);
    margin-bottom: 8px;
}

.static-page-subtitle {
    font-size: 24px;
    font-weight: 600;
    color: var(--green);
    margin-bottom: 32px;
}

.static-page-text {
    font-size: 18px;
    line-height: 1.6;
    color: var(--grey-text);
    margin-bottom: 40px;
    display: flex;
    flex-direction: column;
    gap: 1em;
}

.static-page-content .button {
    height: 44px;
    padding: 0 32px;
}

