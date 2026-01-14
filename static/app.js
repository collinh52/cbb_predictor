// Main application JavaScript

const API_BASE = '/api';

// Load games on page load
document.addEventListener('DOMContentLoaded', () => {
    loadGames();
    
    // Set up refresh button
    document.getElementById('refreshBtn').addEventListener('click', () => {
        loadGames();
    });
});

async function loadGames() {
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const container = document.getElementById('gamesContainer');
    const lastUpdate = document.getElementById('lastUpdate');
    
    loading.style.display = 'block';
    error.style.display = 'none';
    container.innerHTML = '';
    
    try {
        const response = await fetch(`${API_BASE}/games/today`);
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.detail || 'Failed to load games');
        }
        
        loading.style.display = 'none';
        
        if (data.games && data.games.length > 0) {
            data.games.forEach(game => {
                container.appendChild(createGameCard(game));
            });
        } else {
            container.innerHTML = '<div class="no-games">No games scheduled for today.</div>';
        }
        
        lastUpdate.textContent = `Last updated: ${new Date().toLocaleTimeString()}`;
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

