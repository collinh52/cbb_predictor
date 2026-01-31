// Main application JavaScript

const API_BASE = '/api';

// Load games on page load
document.addEventListener('DOMContentLoaded', () => {
    loadGames();
    loadTeams();

    // Set up refresh button
    document.getElementById('refreshBtn').addEventListener('click', () => {
        loadGames(false);
    });

    // Set up force refresh button
    document.getElementById('forceRefreshBtn').addEventListener('click', () => {
        if (confirm('Force regenerate all predictions? This will take longer.')) {
            loadGames(true);
        }
    });

    // Set up navigation
    document.getElementById('todayGamesBtn').addEventListener('click', () => {
        showView('today');
    });

    document.getElementById('rankingsBtn').addEventListener('click', () => {
        showView('rankings');
        loadRankings();
    });

    document.getElementById('customPredictionBtn').addEventListener('click', () => {
        showView('custom');
    });

    // Set up custom prediction form
    document.getElementById('generatePredictionBtn').addEventListener('click', () => {
        generateCustomPrediction();
    });
});

function showView(view) {
    const todayGamesView = document.getElementById('todayGamesView');
    const rankingsView = document.getElementById('rankingsView');
    const customPredictionView = document.getElementById('customPredictionView');
    const todayGamesBtn = document.getElementById('todayGamesBtn');
    const rankingsBtn = document.getElementById('rankingsBtn');
    const customPredictionBtn = document.getElementById('customPredictionBtn');

    // Hide all views
    todayGamesView.style.display = 'none';
    rankingsView.style.display = 'none';
    customPredictionView.style.display = 'none';

    // Remove active class from all buttons
    todayGamesBtn.classList.remove('nav-btn-active');
    rankingsBtn.classList.remove('nav-btn-active');
    customPredictionBtn.classList.remove('nav-btn-active');

    // Show selected view and activate button
    if (view === 'today') {
        todayGamesView.style.display = 'block';
        todayGamesBtn.classList.add('nav-btn-active');
    } else if (view === 'rankings') {
        rankingsView.style.display = 'block';
        rankingsBtn.classList.add('nav-btn-active');
    } else if (view === 'custom') {
        customPredictionView.style.display = 'block';
        customPredictionBtn.classList.add('nav-btn-active');
    }
}

async function loadGames(forceRefresh = false) {
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const container = document.getElementById('gamesContainer');
    const lastUpdate = document.getElementById('lastUpdate');

    loading.style.display = 'block';
    error.style.display = 'none';
    container.innerHTML = '';

    const startTime = Date.now();

    try {
        const url = forceRefresh ? `${API_BASE}/games/today?force_refresh=true` : `${API_BASE}/games/today`;
        const response = await fetch(url);
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.detail || 'Failed to load games');
        }
        
        loading.style.display = 'none';

        const loadTime = ((Date.now() - startTime) / 1000).toFixed(2);

        if (data.games && data.games.length > 0) {
            data.games.forEach(game => {
                container.appendChild(createGameCard(game));
            });
        } else {
            container.innerHTML = '<div class="no-games">No games scheduled for today.</div>';
        }

        const updateText = forceRefresh
            ? `Regenerated at ${new Date().toLocaleTimeString()} (${loadTime}s)`
            : `Loaded at ${new Date().toLocaleTimeString()} (${loadTime}s)`;
        lastUpdate.textContent = updateText;
    } catch (err) {
        loading.style.display = 'none';
        error.style.display = 'block';
        error.textContent = `Error: ${err.message}`;
        console.error('Error loading games:', err);
    }
}

function createGameCard(game) {
    const card = document.createElement('div');
    card.className = 'game-card';
    
    const pred = game.prediction || {};
    
    card.innerHTML = `
        <div class="game-header">
            <div class="matchup">
                <div class="away-team">${escapeHtml(game.away_team || 'Away Team')}</div>
                <div class="vs">@</div>
                <div class="home-team">${escapeHtml(game.home_team || 'Home Team')}</div>
            </div>
            <div class="game-date">${formatDate(game.date)}</div>
        </div>
        
        <div class="prediction-section">
            <div class="section-title">Prediction</div>
            
            <div class="prediction-item">
                <div class="prediction-label">Predicted Winner</div>
                <div class="prediction-value">
                    ${pred.predicted_winner === 'home' ? game.home_team : game.away_team}
                    <span class="winner-badge ${pred.predicted_winner === 'home' ? 'winner-home' : 'winner-away'}">
                        ${pred.predicted_winner === 'home' ? 'Home' : 'Away'}
                    </span>
                </div>
                <div class="prediction-value" style="margin-top: 8px; font-size: 1em;">
                    Margin: ${formatNumber(pred.predicted_margin, 1)} points
                </div>
            </div>
            
            ${pred.spread !== null ? createSpreadPrediction(game, pred) : ''}
            ${pred.total_line !== null ? createTotalPrediction(game, pred) : ''}
            
            <div class="prediction-item" style="margin-top: 15px;">
                <div class="prediction-label">Overall Confidence</div>
                <div class="prediction-value">${formatNumber(pred.overall_confidence || 0, 1)}%</div>
                ${createConfidenceBadge(pred.overall_confidence || 0)}
            </div>
        </div>
    `;
    
    return card;
}

function createSpreadPrediction(game, pred) {
    const homeCovers = pred.home_covers_probability || 0.5;
    const awayCovers = pred.away_covers_probability || 0.5;
    const confidence = pred.home_covers_confidence || 0;
    
    const favoredTeam = pred.spread < 0 ? game.home_team : game.away_team;
    const spreadAbs = Math.abs(pred.spread);
    
    return `
        <div class="prediction-item">
            <div class="prediction-label">Spread: ${favoredTeam} ${pred.spread > 0 ? '+' : ''}${formatNumber(pred.spread, 1)}</div>
            
            <div class="spread-prediction">
                <div>
                    <div class="prediction-label-small">${game.home_team} covers</div>
                    <div class="prediction-value-large">${formatPercent(homeCovers)}</div>
                </div>
                <div>
                    ${createConfidenceBadge(confidence)}
                </div>
            </div>
            
            <div class="probability-bar">
                <div class="probability-fill" style="width: ${homeCovers * 100}%"></div>
            </div>
            
            <div class="spread-prediction" style="margin-top: 8px;">
                <div>
                    <div class="prediction-label-small">${game.away_team} covers</div>
                    <div class="prediction-value-large">${formatPercent(awayCovers)}</div>
                </div>
            </div>
        </div>
    `;
}

function createTotalPrediction(game, pred) {
    const overProb = pred.over_probability || 0.5;
    const underProb = pred.under_probability || 0.5;
    const confidence = pred.over_confidence || 0;
    const predictedTotal = pred.predicted_total || pred.total_line;
    
    return `
        <div class="prediction-item">
            <div class="prediction-label">Total: ${formatNumber(pred.total_line, 1)}</div>
            <div class="prediction-label-small" style="margin-top: 5px;">
                Predicted: ${formatNumber(predictedTotal, 1)} points
            </div>
            
            <div class="total-prediction">
                <div>
                    <div class="prediction-label-small">Over</div>
                    <div class="prediction-value-large">${formatPercent(overProb)}</div>
                </div>
                <div>
                    ${createConfidenceBadge(confidence)}
                </div>
            </div>
            
            <div class="probability-bar">
                <div class="probability-fill" style="width: ${overProb * 100}%"></div>
            </div>
            
            <div class="total-prediction" style="margin-top: 8px;">
                <div>
                    <div class="prediction-label-small">Under</div>
                    <div class="prediction-value-large">${formatPercent(underProb)}</div>
                </div>
            </div>
        </div>
    `;
}

function createConfidenceBadge(confidence) {
    let className = 'confidence-low';
    if (confidence >= 70) {
        className = 'confidence-high';
    } else if (confidence >= 50) {
        className = 'confidence-medium';
    }
    
    return `<span class="confidence-badge ${className}">${formatNumber(confidence, 0)}% confidence</span>`;
}

function formatNumber(num, decimals = 2) {
    if (num === null || num === undefined) return 'N/A';
    return Number(num).toFixed(decimals);
}

function formatPercent(prob) {
    return `${formatNumber(prob * 100, 1)}%`;
}

function formatDate(dateStr) {
    if (!dateStr) return 'TBD';
    try {
        const date = new Date(dateStr);
        return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
    } catch {
        return dateStr;
    }
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Store teams globally for searchable dropdowns
let allTeams = [];

// Load team list for custom prediction
async function loadTeams() {
    try {
        const response = await fetch(`${API_BASE}/teams/list`);
        const data = await response.json();

        if (!response.ok) {
            console.error('Failed to load teams');
            return;
        }

        allTeams = data.teams || [];

        // Initialize searchable dropdowns
        initializeSearchableSelect('away');
        initializeSearchableSelect('home');
    } catch (err) {
        console.error('Error loading teams:', err);
    }
}

// Initialize searchable select dropdown
function initializeSearchableSelect(type) {
    const searchInput = document.getElementById(`${type}TeamSearch`);
    const dropdown = document.getElementById(`${type}TeamDropdown`);
    const hiddenSelect = document.getElementById(`${type}TeamSelect`);

    let highlightedIndex = -1;
    let filteredTeams = [];

    // Handle input changes
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase().trim();

        if (searchTerm === '') {
            // If cleared, reset
            hiddenSelect.value = '';
            searchInput.classList.remove('has-value');
            dropdown.style.display = 'none';
            return;
        }

        // Filter teams
        filteredTeams = allTeams.filter(team =>
            team.name.toLowerCase().includes(searchTerm)
        );

        // Display filtered teams
        displayFilteredTeams(filteredTeams, dropdown, searchInput, hiddenSelect, type);
        highlightedIndex = -1;
    });

    // Handle focus
    searchInput.addEventListener('focus', () => {
        if (searchInput.value.trim() !== '' && hiddenSelect.value === '') {
            // Show dropdown if there's text but no selection
            const searchTerm = searchInput.value.toLowerCase().trim();
            filteredTeams = allTeams.filter(team =>
                team.name.toLowerCase().includes(searchTerm)
            );
            displayFilteredTeams(filteredTeams, dropdown, searchInput, hiddenSelect, type);
        }
    });

    // Handle keyboard navigation
    searchInput.addEventListener('keydown', (e) => {
        if (dropdown.style.display === 'none') return;

        const items = dropdown.querySelectorAll('.searchable-select-dropdown-item:not(.searchable-select-dropdown-no-results)');

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            highlightedIndex = Math.min(highlightedIndex + 1, items.length - 1);
            updateHighlight(items, highlightedIndex);
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            highlightedIndex = Math.max(highlightedIndex - 1, 0);
            updateHighlight(items, highlightedIndex);
        } else if (e.key === 'Enter') {
            e.preventDefault();
            if (highlightedIndex >= 0 && items[highlightedIndex]) {
                items[highlightedIndex].click();
            }
        } else if (e.key === 'Escape') {
            dropdown.style.display = 'none';
            highlightedIndex = -1;
        }
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
            highlightedIndex = -1;
        }
    });
}

// Display filtered teams in dropdown
function displayFilteredTeams(teams, dropdown, searchInput, hiddenSelect, type) {
    dropdown.innerHTML = '';

    if (teams.length === 0) {
        dropdown.innerHTML = '<div class="searchable-select-dropdown-no-results">No teams found</div>';
        dropdown.style.display = 'block';
        return;
    }

    teams.forEach((team, index) => {
        const item = document.createElement('div');
        item.className = 'searchable-select-dropdown-item';
        item.textContent = team.name;
        item.dataset.teamId = team.id;
        item.dataset.teamName = team.name;

        item.addEventListener('click', () => {
            selectTeam(team, searchInput, hiddenSelect, dropdown, type);
        });

        dropdown.appendChild(item);
    });

    dropdown.style.display = 'block';
}

// Select a team
function selectTeam(team, searchInput, hiddenSelect, dropdown, type) {
    searchInput.value = team.name;
    searchInput.classList.add('has-value');
    hiddenSelect.value = team.id;
    dropdown.style.display = 'none';
}

// Update highlighted item in dropdown
function updateHighlight(items, index) {
    items.forEach((item, i) => {
        if (i === index) {
            item.classList.add('highlighted');
            item.scrollIntoView({ block: 'nearest' });
        } else {
            item.classList.remove('highlighted');
        }
    });
}

// Generate custom prediction
async function generateCustomPrediction() {
    const homeTeamId = document.getElementById('homeTeamSelect').value;
    const awayTeamId = document.getElementById('awayTeamSelect').value;
    const neutralCourt = document.getElementById('neutralCourt').checked;

    const loading = document.getElementById('customLoading');
    const error = document.getElementById('customError');
    const result = document.getElementById('customPredictionResult');

    // Validation
    if (!homeTeamId || !awayTeamId) {
        error.style.display = 'block';
        error.textContent = 'Please select both home and away teams';
        return;
    }

    if (homeTeamId === awayTeamId) {
        error.style.display = 'block';
        error.textContent = 'Please select different teams';
        return;
    }

    loading.style.display = 'block';
    error.style.display = 'none';
    result.innerHTML = '';

    try {
        const response = await fetch(`${API_BASE}/predictions/custom`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                home_team_id: parseInt(homeTeamId),
                away_team_id: parseInt(awayTeamId),
                neutral_court: neutralCourt
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'Failed to generate prediction');
        }

        loading.style.display = 'none';
        displayCustomPrediction(data);
    } catch (err) {
        loading.style.display = 'none';
        error.style.display = 'block';
        error.textContent = `Error: ${err.message}`;
        console.error('Error generating prediction:', err);
    }
}

// Display custom prediction results
function displayCustomPrediction(data) {
    const result = document.getElementById('customPredictionResult');

    const pred = data.prediction || {};
    const homeStats = data.home_team_stats || {};
    const awayStats = data.away_team_stats || {};

    result.innerHTML = `
        <div class="game-card">
            <div class="game-header">
                <div class="matchup">
                    <div class="away-team">${escapeHtml(data.away_team)}</div>
                    <div class="vs">@</div>
                    <div class="home-team">${escapeHtml(data.home_team)}</div>
                    ${data.neutral_court ? '<div class="neutral-badge">Neutral Court</div>' : ''}
                </div>
            </div>

            <div class="prediction-section">
                <div class="section-title">Prediction Results</div>

                <div class="prediction-details">
                    <div class="details-grid">
                        <div class="detail-card">
                            <div class="detail-title">Predicted Winner</div>
                            <div class="detail-value">
                                ${pred.predicted_winner === 'home' ? data.home_team : data.away_team}
                                <span class="winner-badge ${pred.predicted_winner === 'home' ? 'winner-home' : 'winner-away'}">
                                    ${pred.predicted_winner === 'home' ? 'Home' : 'Away'}
                                </span>
                            </div>
                        </div>

                        <div class="detail-card">
                            <div class="detail-title">Predicted Margin</div>
                            <div class="detail-value">${formatNumber(pred.predicted_margin, 1)} points</div>
                        </div>

                        <div class="detail-card">
                            <div class="detail-title">Predicted Total</div>
                            <div class="detail-value">${formatNumber(pred.predicted_total, 1)} points</div>
                        </div>

                        <div class="detail-card">
                            <div class="detail-title">Confidence</div>
                            <div class="detail-value">${formatNumber(pred.overall_confidence || 0, 1)}%</div>
                        </div>
                    </div>
                </div>

                ${pred.predicted_margin ? createCustomPredictionBreakdown(pred) : ''}
            </div>
        </div>

        ${createTeamStatsComparison(data.home_team, homeStats, data.away_team, awayStats)}
    `;
}

function createCustomPredictionBreakdown(pred) {
    return `
        <div class="prediction-details" style="margin-top: 20px;">
            <div class="section-title">Prediction Breakdown</div>
            <div class="details-grid">
                ${pred.ukf_predicted_margin !== undefined ? `
                    <div class="detail-card">
                        <div class="detail-title">UKF Margin</div>
                        <div class="detail-value">${formatNumber(pred.ukf_predicted_margin, 1)}</div>
                    </div>
                ` : ''}
                ${pred.ml_predicted_margin !== undefined && pred.ml_predicted_margin !== null ? `
                    <div class="detail-card">
                        <div class="detail-title">ML Margin</div>
                        <div class="detail-value">${formatNumber(pred.ml_predicted_margin, 1)}</div>
                    </div>
                ` : ''}
                ${pred.ukf_predicted_total !== undefined ? `
                    <div class="detail-card">
                        <div class="detail-title">UKF Total</div>
                        <div class="detail-value">${formatNumber(pred.ukf_predicted_total, 1)}</div>
                    </div>
                ` : ''}
                ${pred.ml_predicted_total !== undefined && pred.ml_predicted_total !== null ? `
                    <div class="detail-card">
                        <div class="detail-title">ML Total</div>
                        <div class="detail-value">${formatNumber(pred.ml_predicted_total, 1)}</div>
                    </div>
                ` : ''}
            </div>
        </div>
    `;
}

function createTeamStatsComparison(homeTeam, homeStats, awayTeam, awayStats) {
    return `
        <div class="team-stats">
            <div class="team-stat-card">
                <div class="team-stat-header">${escapeHtml(homeTeam)}</div>
                ${createTeamStatRows(homeStats)}
            </div>

            <div class="team-stat-card">
                <div class="team-stat-header">${escapeHtml(awayTeam)}</div>
                ${createTeamStatRows(awayStats)}
            </div>
        </div>
    `;
}

function createTeamStatRows(stats) {
    const rows = [];

    if (stats.offensive_rating !== undefined) {
        rows.push(`
            <div class="stat-row">
                <span class="stat-label">Offensive Rating</span>
                <span class="stat-value">${formatNumber(stats.offensive_rating, 1)}</span>
            </div>
        `);
    }

    if (stats.defensive_rating !== undefined) {
        rows.push(`
            <div class="stat-row">
                <span class="stat-label">Defensive Rating</span>
                <span class="stat-value">${formatNumber(stats.defensive_rating, 1)}</span>
            </div>
        `);
    }

    if (stats.pace !== undefined) {
        rows.push(`
            <div class="stat-row">
                <span class="stat-label">Pace</span>
                <span class="stat-value">${formatNumber(stats.pace, 1)}</span>
            </div>
        `);
    }

    if (stats.kenpom_adj_em !== undefined && stats.kenpom_adj_em !== 0) {
        rows.push(`
            <div class="stat-row">
                <span class="stat-label">KenPom Adj EM</span>
                <span class="stat-value">${formatNumber(stats.kenpom_adj_em, 1)}</span>
            </div>
        `);
    }

    if (stats.kenpom_adj_o !== undefined && stats.kenpom_adj_o !== 100) {
        rows.push(`
            <div class="stat-row">
                <span class="stat-label">KenPom Adj O</span>
                <span class="stat-value">${formatNumber(stats.kenpom_adj_o, 1)}</span>
            </div>
        `);
    }

    if (stats.kenpom_adj_d !== undefined && stats.kenpom_adj_d !== 100) {
        rows.push(`
            <div class="stat-row">
                <span class="stat-label">KenPom Adj D</span>
                <span class="stat-value">${formatNumber(stats.kenpom_adj_d, 1)}</span>
            </div>
        `);
    }

    if (stats.momentum !== undefined) {
        rows.push(`
            <div class="stat-row">
                <span class="stat-label">Momentum</span>
                <span class="stat-value">${formatNumber(stats.momentum, 2)}</span>
            </div>
        `);
    }

    if (stats.fatigue !== undefined) {
        rows.push(`
            <div class="stat-row">
                <span class="stat-label">Fatigue</span>
                <span class="stat-value">${formatNumber(stats.fatigue, 2)}</span>
            </div>
        `);
    }

    if (stats.sos !== undefined) {
        rows.push(`
            <div class="stat-row">
                <span class="stat-label">Strength of Schedule</span>
                <span class="stat-value">${formatNumber(stats.sos, 1)}</span>
            </div>
        `);
    }

    if (rows.length === 0) {
        return '<div class="stat-row"><span class="stat-label">No detailed stats available</span></div>';
    }

    return rows.join('');
}

// ==================== RANKINGS PAGE ====================

let rankingsData = [];
let currentSortColumn = 'rank';
let currentSortDirection = 'asc';

async function loadRankings() {
    const loading = document.getElementById('rankingsLoading');
    const error = document.getElementById('rankingsError');
    const tableContainer = document.getElementById('rankingsTableContainer');

    loading.style.display = 'block';
    error.style.display = 'none';
    tableContainer.style.display = 'none';

    try {
        const response = await fetch(`${API_BASE}/teams/rankings`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'Failed to load rankings');
        }

        rankingsData = data.teams || [];
        currentSortColumn = 'rank';
        currentSortDirection = 'asc';

        renderRankingsTable();

        loading.style.display = 'none';
        tableContainer.style.display = 'block';

        // Set up sorting listeners
        setupRankingsSortListeners();
    } catch (err) {
        loading.style.display = 'none';
        error.style.display = 'block';
        error.textContent = `Error: ${err.message}`;
        console.error('Error loading rankings:', err);
    }
}

function setupRankingsSortListeners() {
    const headers = document.querySelectorAll('#rankingsTable th.sortable');
    headers.forEach(header => {
        header.addEventListener('click', () => {
            const column = header.getAttribute('data-sort');
            sortRankings(column);
        });
    });
}

function sortRankings(column) {
    // Toggle direction if clicking same column
    if (column === currentSortColumn) {
        currentSortDirection = currentSortDirection === 'asc' ? 'desc' : 'asc';
    } else {
        currentSortColumn = column;
        // Default sort direction based on column
        if (column === 'rank' || column === 'defensive_rating' || column === 'adj_d') {
            currentSortDirection = 'asc'; // Lower is better for rank and defense
        } else {
            currentSortDirection = 'desc'; // Higher is better for most stats
        }
    }

    // Sort data
    rankingsData.sort((a, b) => {
        let aVal = a[column];
        let bVal = b[column];

        // Handle string vs number comparison
        if (typeof aVal === 'string' && typeof bVal === 'string') {
            aVal = aVal.toLowerCase();
            bVal = bVal.toLowerCase();
        }

        if (currentSortDirection === 'asc') {
            return aVal > bVal ? 1 : aVal < bVal ? -1 : 0;
        } else {
            return aVal < bVal ? 1 : aVal > bVal ? -1 : 0;
        }
    });

    renderRankingsTable();
}

function renderRankingsTable() {
    const tbody = document.getElementById('rankingsTableBody');
    tbody.innerHTML = '';

    // Update header sort indicators
    const headers = document.querySelectorAll('#rankingsTable th.sortable');
    headers.forEach(header => {
        header.classList.remove('active', 'sort-asc', 'sort-desc');
        if (header.getAttribute('data-sort') === currentSortColumn) {
            header.classList.add('active', currentSortDirection === 'asc' ? 'sort-asc' : 'sort-desc');
        }
    });

    // Render rows
    rankingsData.forEach((team, index) => {
        const row = document.createElement('tr');

        // Add hover effect class
        row.className = 'rankings-row';

        row.innerHTML = `
            <td>${index + 1}</td>
            <td class="team-name-cell">${escapeHtml(team.team_name)}</td>
            <td>${escapeHtml(team.conference || '-')}</td>
            <td>${team.record || '0-0'}</td>
            <td>${formatNumber(team.adj_em, 1)}</td>
            <td>${formatNumber(team.adj_o, 1)}</td>
            <td>${formatNumber(team.adj_d, 1)}</td>
            <td>${formatNumber(team.adj_t, 1)}</td>
            <td>${formatNumber(team.offensive_rating, 1)}</td>
            <td>${formatNumber(team.defensive_rating, 1)}</td>
            <td>${formatNumber(team.pace, 1)}</td>
            <td>${formatMomentum(team.momentum)}</td>
        `;

        tbody.appendChild(row);
    });
}

function formatMomentum(momentum) {
    if (momentum === undefined || momentum === null) {
        return '-';
    }
    const formatted = formatNumber(momentum, 2);
    if (momentum > 0.2) {
        return `<span style="color: #4CAF50; font-weight: 600;">+${formatted}</span>`;
    } else if (momentum < -0.2) {
        return `<span style="color: #f44336; font-weight: 600;">${formatted}</span>`;
    } else {
        return formatted;
    }
}

