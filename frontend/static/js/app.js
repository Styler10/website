async function loadProducts() {
    const res = await fetch('/api/products');
    const products = await res.json();

    const container = document.getElementById('products');
    if (!container) return;

    container.innerHTML = '';

    products.forEach(p => {
        const card = document.createElement('div');
        card.className = 'product-card';

        card.innerHTML = `
            <img src="${p.image}" alt="${p.name}">
            <h3>${p.name}</h3>
            <p class="price">${p.price} ₽</p>
            <button onclick="addToCart(${p.id})">В корзину</button>
        `;

        container.appendChild(card);
    });
}

async function addToCart(id) {
    await fetch('/api/cart', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ product_id: id })
    });
}

async function clearCart() {
    await fetch('/api/cart/clear', {
        method: 'POST'
    });

    loadCart();
}



async function loadCart() {
    const res = await fetch('/api/cart');
    const items = await res.json();

    const ul = document.getElementById('cart');
    if (!ul) return;

    ul.innerHTML = '';

    items.forEach(i => {
        const li = document.createElement('li');
        li.textContent = `${i.name} x${i.quantity} = ${i.price * i.quantity}`;
        ul.appendChild(li);
    });
}
