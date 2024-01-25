<template>
    <div class="container">
        <canvas id="myChart"></canvas>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
name: 'AdminGraphView',
mounted() {
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of ',
                data: [12, 19, 3, 5, 2, 3],
                borderWidth: 1,
            }],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
},
}
</script>