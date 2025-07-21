function getQuote() {
  const quotes = [
    "Rise and grind, sigma. The smurf cat believes in your hustle today",
        "If you’re feeling down, just remember: even John Pork kept calling",
        "Don’t let Monday leave you broken — go hit the griddy instead",
        "You got this, king. Kai Cenat didn’t stream 24 hours for you to give up",
        "Today’s vibe: bussin' through the cringe like a goofy ahh gladiator"
        "Be the biggest bird. Not just a bird... the BIGGEST"
        "Remember: Livvy Dunne didn't rizz up Baby Gronk for you to skip leg day"
        "Goon cave is temporary, but the grindset is eternal"
        "If you’re ever lost, just ask: 'Did you pray today?' and follow the pibby glitch"
        "Never forget: hit or miss, I guess they never miss huh... but you? You never miss"
        "Keep pushing, king. Andrew Tate is somewhere doing pushups in Crocs for you"
  ];
  const randomIndex = Math.floor(Math.random() * quotes.length);
  document.getElementById("quote-text").textContent = quotes[randomIndex];
}
