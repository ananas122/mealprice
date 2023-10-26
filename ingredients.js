document.addEventListener("DOMContentLoaded", function() {
  console.log("Document chargé");
  let editingRow = null;
  const ingredientTable = document.getElementById("ingredientTable").getElementsByTagName('tbody')[0];
  const categoryFilter = document.getElementById("category");
  const sortSelect = document.getElementById("sort");
  const sortButton = document.getElementById("sortButton");
  const sortOrderSelect = document.getElementById("sortOrder");

  // Fonction pour ajouter une nouvelle ligne d'ingrédient
  function addIngredientRow() {
        console.log("Ajout d'une nouvelle ligne"); // Ajout d'un console.log
    const newRow = ingredientTable.insertRow();
    newRow.innerHTML = `
      <td><i class="fas fa-edit editIcon"></i> <i class="fas fa-trash-alt deleteIcon"></i></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    `;
    return newRow;
  }

  // Fonction pour mettre à jour une ligne d'ingrédient avec les données fournies
  function updateRow(row) {
    console.log("Mise à jour de la ligne");
    const name = document.getElementById("name").value;
    const category = document.getElementById("category").value;
    const supplier = document.getElementById("supplier").value;
    const unit_cost = parseFloat(document.getElementById("unit_cost").value);
    const stock_quantity = parseInt(document.getElementById("stock_quantity").value);

    row.cells[1].textContent = name;
    row.cells[2].textContent = category;
    row.cells[3].textContent = supplier;
    row.cells[4].textContent = unit_cost;
    row.cells[5].textContent = stock_quantity;
  }

  // Gestionnaire d'événement pour le bouton "Ajouter"
  document.getElementById("addIngredient").addEventListener("click", function() {
        console.log("Bouton Ajouter cliqué"); // Ajout d'un console.log

    // Récupérez les valeurs des champs de saisie
    const name = document.getElementById("name").value;
    const category = document.getElementById("category").value;
    const supplier = document.getElementById("supplier").value;
    const unit_cost = parseFloat(document.getElementById("unit_cost").value);
    const stock_quantity = parseInt(document.getElementById("stock_quantity").value);
// Vérifiez que tous les champs ont été remplis avant l'ajout du nouveau produit
    const newRow = addIngredientRow();
    // Mettez à jour la ligne existante
    updateRow(newRow);

    // Définissez les valeurs des cellules de la nouvelle ligne
    newRow.cells[1].textContent = name;
    newRow.cells[2].textContent = category;
    newRow.cells[3].textContent = supplier;
    newRow.cells[4].textContent = unit_cost;
    newRow.cells[5].textContent = stock_quantity;
  });

  // Gestionnaire d'événement pour le bouton "Trier"
  sortButton.addEventListener("click", function() {
    const sortField = sortSelect.value;
    const sortOrder = sortOrderSelect.value;
    const rows = Array.from(ingredientTable.rows).slice(1); // Ignorer la première ligne d'en-tête
    rows.sort((a, b) => {
      const cellA = a.cells[sortField === "name" ? 1 : 2].textContent.toLowerCase();
      const cellB = b.cells[sortField === "name" ? 1 : 2].textContent.toLowerCase();
      return sortOrder === "asc" ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
    });
    while (ingredientTable.rows.length > 1) {
      ingredientTable.deleteRow(1);
    }
    rows.forEach(row => ingredientTable.appendChild(row));
  });

  // Gestionnaire d'événement pour la sélection de catégorie
  categoryFilter.addEventListener("change", function() {
    const selectedCategory = categoryFilter.value;
    const rows = Array.from(ingredientTable.rows).slice(1);
    rows.forEach(row => {
      const category = row.cells[2].textContent;
      row.style.display = selectedCategory === "" || category === selectedCategory ? "" : "none";
    });
  });

  // Gestionnaire d'événement pour le bouton "Modifier"
  document.getElementById("updateIngredient").addEventListener("click", function() {
    if (editingRow) {
      updateRow(editingRow);
      editingRow = null;
      alert("Ligne mise à jour avec succès !");
    } else {
      alert("Veuillez sélectionner une ligne à modifier en cliquant sur l'icône de modification.");
    }
  });

  // Gestionnaire d'événement pour les icônes d'édition et de suppression
  ingredientTable.addEventListener("click", function(event) {
    const target = event.target;
    if (target.classList.contains("editIcon")) {
      editingRow = target.closest("tr");
      document.getElementById("name").value = editingRow.cells[1].textContent;
      categoryFilter.value = editingRow.cells[2].textContent;
      document.getElementById("supplier").value = editingRow.cells[3].textContent;
      document.getElementById("unit_cost").value = editingRow.cells[4].textContent;
      document.getElementById("stock_quantity").value = editingRow.cells[5].textContent;
    } else if (target.classList.contains("deleteIcon")) {
      editingRow = null;
      target.closest("tr").remove();
    }
  });

  $(document).ready(function() {
    $("#ingredients-link").click(function(e) { // Utilisation de l'ID pour cibler le lien "Ingredients"
      e.preventDefault();
      $.get("/ingredients.html", function(data) {
        $("#ingredientsContainer").html(data);
      }).fail(function() {
        console.log("Erreur lors du chargement de la page Ingredients.");
      });
    });
  });

});
