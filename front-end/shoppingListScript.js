// Define the server URL variable
const serverURL = 'http://127.0.0.1:4999';

document.addEventListener("DOMContentLoaded", function () {
    // Add event listener to the button
    document.getElementById('display-list-btn').addEventListener('click', function () {
        // Get the selected shopper ID
        const selectedShopperId = document.getElementById('shopper-dropdown').value;

        // Fetch the shopping list for the selected shopper
        fetch(`${serverURL}/getShoppingList?shopper_id=${selectedShopperId}`)
            .then(response => response.json())
            .then(shoppingList => {
                const shoppingListTable = document.getElementById('shopping-list-table');
                // Clear existing rows in the table
                shoppingListTable.innerHTML = '';

                shoppingList.forEach(item => {
                    const row = shoppingListTable.insertRow();
                    const cell1 = row.insertCell(0);
                    const cell2 = row.insertCell(1);
                    const cell3 = row.insertCell(3)

                    cell1.textContent = item.item_id;
                    cell2.textContent = item.name;
                    cell3.textContent = item.item_price;
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});
