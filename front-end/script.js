// Define the server URL variable
const serverURL = 'http://127.0.0.1:4999';

document.addEventListener("DOMContentLoaded", function () {
    // Populate shoppers dropdown
    fetch('${serverURL}/getShoppers')
        .then(response => response.json())
        .then(shoppers => {
            const shopperDropdown = document.getElementById('shopper-dropdown');
            shoppers.forEach(shopper => {
                const option = document.createElement('option');
                option.value = shopper.shopper_id;
                option.text = shopper.name;
                shopperDropdown.add(option);
            });
        });

    // Populate items table
    fetch('${serverURL}/getProducts')
        .then(response => response.json())
        .then(items => {
            const itemList = document.getElementById('items');
            items.forEach(item => {
                const row = itemList.insertRow();
                const cell1 = row.insertCell(0);
                const cell2 = row.insertCell(1);
                const cell3 = row.insertCell(2);
                const cell4 = row.insertCell(3)

                cell1.textContent = item.item_id;
                cell2.textContent = item.name;
                cell3.textContent = item.price;

                const addToCartButton = document.createElement('button');
                addToCartButton.textContent = 'Add to Cart';
                addToCartButton.addEventListener('click', function () {
                    addToShoppingList(item.item_id);
                });

                cell4.appendChild(addToCartButton);
            });
        });

    // Add to Shopping List button click event
    document.getElementById('add-to-list-btn').addEventListener('click', addToShoppingList);
});

function addToShoppingList() {
    const selectedShopper = document.getElementById('shopper-dropdown').value;
    const selectedItems = getSelectedItems();

    fetch('${serverURL}/addItemsToShoppingList', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            shopper_id: selectedShopper,
            item_ids: selectedItems,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.message.includes("violate the constraint")) {
            alert(data.message);  // Display constraint violation message as a pop-up
        } else {
            console.log(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function getSelectedItems() {
    const selectedItems = [];
    const checkboxes = document.querySelectorAll('#items input[type="checkbox"]:checked');
    checkboxes.forEach(checkbox => {
        selectedItems.push(checkbox.value);
    });
    return selectedItems;
}
