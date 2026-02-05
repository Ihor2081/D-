const API_URL = "http://127.0.0.1:8000/api/products";
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("productForm");

    if (!form) {
        console.error("productForm not found");
        return;
    }

    form.addEventListener("submit", handleSubmit);

    loadProducts();
});

/* ===================== LOAD ===================== */

function loadProducts() {
    fetch(API_URL)
        .then(res => {
            if (!res.ok) throw new Error("Failed to load products");
            return res.json();
        })
        .then(renderProducts)
        .catch(err => console.error(err));
}

/* ===================== RENDER ===================== */

function renderProducts(products) {
    const ul = document.getElementById("productList");
    ul.innerHTML = "";

    products.forEach(product => {
        const li = document.createElement("li");

        const text = document.createElement("span");
        text.textContent =
            `${product.name} (${product.model}) — ${product.price}$ × ${product.quantity}`;

        const editBtn = document.createElement("button");
        editBtn.textContent = "✏️ Edit";
        editBtn.addEventListener("click", () => startEdit(product));

        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "🗑";
        deleteBtn.addEventListener("click", () => deleteProduct(product.id));

        li.appendChild(text);
        li.appendChild(editBtn);
        li.appendChild(deleteBtn);

        ul.appendChild(li);
    });
}

/* ===================== ADD / UPDATE ===================== */

function handleSubmit(e) {
    e.preventDefault();

    const form = e.target;
    const id = form.dataset.editId;

    const product = {
        name: form.name.value.trim(),
        model: form.model.value.trim(),
        price: Number(form.price.value),
        quantity: Number(form.quantity.value)
    };

    if (!product.name || !product.model || product.price <= 0 || product.quantity <= 0) {
        alert("Invalid input");
        return;
    }

    const method = id ? "PUT" : "POST";
    const url = id ? `${API_URL}/${id}` : API_URL;

    fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(product)
    })
    .then(res => {
        if (!res.ok) throw new Error("Save failed");
        return res.json();
    })
    .then(() => {
        resetForm();
        loadProducts();
    })
    .catch(err => console.error(err));
}

/* ===================== EDIT ===================== */

function startEdit(product) {
    const form = document.getElementById("productForm");

    form.name.value = product.name;
    form.model.value = product.model;
    form.price.value = product.price;
    form.quantity.value = product.quantity;

    form.dataset.editId = product.id;

    document.getElementById("submitBtn").textContent = "Update product";
}

/* ===================== DELETE ===================== */

function deleteProduct(id) {
    if (!confirm("Delete this product?")) return;

    fetch(`${API_URL}/${id}`, { method: "DELETE" })
        .then(res => {
            if (!res.ok) throw new Error("Delete failed");
            return res.json();
        })
        .then(loadProducts)
        .catch(err => console.error(err));
}

/* ===================== HELPERS ===================== */

function resetForm() {
    const form = document.getElementById("productForm");
    form.reset();
    delete form.dataset.editId;
    document.getElementById("submitBtn").textContent = "Add product";
}