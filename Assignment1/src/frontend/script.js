let myChart;

function updateArbitrageData() {
    fetch('/arbitrage')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log('Data received:', data);
            let resultDiv = document.getElementById('results');
            let status = document.getElementById('status');
            
            if (data.error) {
                status.textContent = data.error;
            } else if (data.message) {
                status.textContent = data.message;
            } else {
                status.textContent = "Arbitrage Opportunity Found!";
                resultDiv.innerHTML = `
                    <p>Solana Price: ${data.solana_price} USD</p>
                    <p>Base Price: ${data.base_price} USD</p>
                    <p>Net Profit: ${data.net_profit} USD per token</p>
                `;
                
                updateChart(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('status').textContent = 'Error fetching data: ' + error;
        });
}

function updateChart(data) {
    console.log('Updating chart with data:', data);
    const ctx = document.getElementById('chart').getContext('2d');
    if (!ctx) {
        console.error('Chart context not found');
        return;
    }

    const chartData = {
        labels: ['Solana Price', 'Base Price', 'Net Profit'],
        datasets: [{
            label: 'Arbitrage Data',
            data: [data.solana_price, data.base_price, data.net_profit],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    };

    // Check if the chart already exists
    if (myChart) {
        myChart.destroy();
    }

    // Create the new chart
    try {
        myChart = new Chart(ctx, {
            type: 'bar',
            data: chartData,
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } catch (error) {
        console.error('Error creating chart:', error);
    }
}

// Initial data fetch when the page loads
document.addEventListener('DOMContentLoaded', (event) => {
    console.log("Fetching initial data...");
    updateArbitrageData();
});

// Update every 5 seconds
// Update every 15 seconds
setInterval(updateArbitrageData, 20000);
