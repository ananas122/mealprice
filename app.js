document.addEventListener('DOMContentLoaded', function() {
    const addIngredientButton = document.getElementById('addIngredient');
    const ingredientTable = document.getElementById('ingredientTable');

    addIngredientButton.addEventListener('click', function() {
        const name = document.getElementById('name').value;
        const reference = document.getElementById('reference').value;
        const category = document.getElementById('category').value;
        const supplier = document.getElementById('supplier').value;
        const unitCost = document.getElementById('unit_cost').value;
        const stockQuantity = document.getElementById('stock_quantity').value;

        // Créer une nouvelle ligne pour le tableau
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${name}</td>
            <td>${reference}</td>
            <td>${category}</td>
            <td>${supplier}</td>
            <td>${unitCost}</td>
            <td>${stockQuantity}</td>
            <td>...</td> <!-- Ajoutez ici l'évolution -->
        `;

        // Ajouter la nouvelle ligne au tableau
        ingredientTable.appendChild(row);

        // Effacer les champs du formulaire
        document.getElementById('name').value = '';
        document.getElementById('reference').value = '';
        document.getElementById('category').value = '';
        document.getElementById('supplier').value = '';
        document.getElementById('unit_cost').value = '';
        document.getElementById('stock_quantity').value = '';

        // Envoi des données au serveur Flask pour enregistrement
        fetch('/add_ingredient', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                reference: reference,
                category: category,
                supplier: supplier,
                unit_cost: unitCost,
                stock_quantity: stockQuantity
            })
        })
        .then(response => {
            if (response.ok) {
                // Réalisez des actions supplémentaires si nécessaire
            } else {
                console.error('Erreur lors de l\'enregistrement des données');
            }
        })
        .catch(error => {
            console.error('Erreur lors de l\'enregistrement des données', error);
        });
    });
});
document.getElementById("loginBtn").addEventListener("click", function() {
    // Redirigez l'utilisateur vers la page de connexion
    window.location.href = "/login";
});

document.getElementById("signupBtn").addEventListener("click", function() {
    // Redirigez l'utilisateur vers la page d'inscription
    window.location.href = "/signup";
});

document.getElementById("gmailLoginBtn").addEventListener("click", function() {
    // Redirigez l'utilisateur vers la page d'authentification Gmail
    window.location.href = "/auth/gmail";
});

document.getElementById("facebookLoginBtn").addEventListener("click", function() {
    // Redirigez l'utilisateur vers la page d'authentification Facebook
    window.location.href = "/auth/facebook";
});
