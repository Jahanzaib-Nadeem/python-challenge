The frontend of the application is built with React and uses Stripe for handling subscriptions. Here's a high-level overview of how it works

## User Authentication: 
The application uses a custom hook, useAuth, to manage user authentication. This hook provides user information and subscription details to other components.

## Subscription Management: 
The usePay hook is used to handle the subscription payment process. It uses the useAuth hook to get the user's information and checks if the user is logged in before proceeding. Depending on the subscription type (individual, group, or business) and the app type (world or universe), it sets the price for the subscription. It then redirects the user to the Stripe checkout page.

## Stripe Integration: 
The getStripe function from `client/src/lib/getStripe.js` is used to initialize the Stripe object. This object is used in the usePay hook to redirect the user to the Stripe checkout page.

## Subscription Status: 
After the user has completed the payment process on the Stripe checkout page, they are redirected back to the application. The useStripe hook is used to fetch the user's subscription status from the server. If the user has an active subscription, the subscription details are displayed on the HelloWorld page.

## Server-side Subscription Handling: 
On the server side, the getSubscriptions function in `server/user/views.py` is used to fetch the user's subscriptions from Stripe. It searches for the user's email in the Stripe Customer object, retrieves the subscriptions for that customer, and returns the active subscriptions.