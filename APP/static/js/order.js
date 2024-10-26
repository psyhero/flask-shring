const count = document.querySelector('.content_order form input[name="amount"]')
const price = document.querySelector('.content_order form span.price')

count.addEventListener('input', function () {
    price.textContent = (count.value * 0.01).toFixed(2)
})