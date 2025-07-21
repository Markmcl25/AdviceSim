async function getQuote() {
    const response = await fetch('/quote');
    const data = await response.json();
    document.getElementById('quote-text').innerText = data.quote;
}
