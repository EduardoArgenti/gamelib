const API_URL = "http://localhost:8000";

let games = [];


async function loadGames() {
    const gamesList = document.getElementById("games-list");
    const gamesCount = document.getElementById("games-count");

    gamesList.innerHTML = `
        <div class="col-12 loading">
            Loading games...
        </div>
    `;

    try {
        const response = await fetch(`${API_URL}/games`);

        if (!response.ok) {
            throw new Error("Failed to load games");
        }

        games = await response.json();

        gamesCount.textContent = `${games.length} games`;

        renderGames(games);

    } catch (error) {
        console.error(error);

        gamesList.innerHTML = `
            <div class="col-12 error">
                Failed to load games.
            </div>
        `;
    }
}


function renderGames(gamesToRender) {
    const gamesList = document.getElementById("games-list");

    gamesList.innerHTML = "";

    if (gamesToRender.length === 0) {
        gamesList.innerHTML = `
            <div class="col-12 loading">
                No games found.
            </div>
        `;

        return;
    }

    gamesToRender.forEach(game => {

        const keywords = game.keywords
            .slice(0, 3)
            .map(keyword => `
                <span class="keyword">
                    ${keyword}
                </span>
            `)
            .join("");


        const card = `
            <div class="col-6 col-md-4 col-lg-3 col-xl-2">

                <div class="game-card">

                    <img
                        class="game-cover"
                        src="http://localhost:8000${game.cover_url}"
                        alt="${game.name}"
                    >

                    <div class="game-title">
                        ${game.name}
                    </div>

                    <div class="game-developer">
                        ${game.developer}
                    </div>

                    <div class="game-keywords">
                        ${keywords}
                    </div>

                </div>

            </div>
        `;

        gamesList.innerHTML += card;
    });
}


function searchGames(event) {
    const searchTerm = event.target.value.toLowerCase();

    const filteredGames = games.filter(game =>
        game.name.toLowerCase().includes(searchTerm)
    );

    renderGames(filteredGames);
}


document
    .getElementById("search-input")
    .addEventListener("input", searchGames);


loadGames();