import * as echarts from 'echarts';

var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

option = {
    title: {
        text: '2024转专业报名'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {},
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: { readOnly: false },
            magicType: { type: ['line', 'bar'] },
            restore: {},
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: 'false',
        data: [
            '10:44',
            '14:17',
            '15:07',
            '15:20',
            '15:48',
            '16:01',
            '16:02',
            '16:43'
        ]
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value} 人'
        }
    },
    series: [
        {
            name: '计科',
            type: 'line',
            data: [36, 39, 39, 38, 39, 39, 39, 40],
            markPoint: {
                data: [
                    { type: 'max', name: '最大值' },
                    { type: 'min', name: '最小值' }
                ]
            },
            markLine: {
                data: [{ type: 'average', name: '平均值' }]
            }
        },
        {
            name: '大数据',
            type: 'line',
            data: [9, 12, 12, 12, 12, 12, 13, 13],
            markPoint: {
                data: [
                    { type: 'max', name: '最大值' },
                    { type: 'min', name: '最小值' }
                ]
            },
            markLine: {
                data: [{ type: 'average', name: '平均值' }]
            }
        },
        {
            name: '人工智能',
            type: 'line',
            data: [10, 13, 13, 13, 14, 14, 16, 16],
            markPoint: {
                data: [
                    { type: 'max', name: '最大值' },
                    { type: 'min', name: '最小值' }
                ]
            },
            markLine: {
                data: [{ type: 'average', name: '平均值' }]
            }
        },
        {
            name: '软工',
            type: 'line',
            data: [11, 13, 12, 12, 12, 13, 15, 15],
            markPoint: {
                data: [
                    { type: 'max', name: '最大值' },
                    { type: 'min', name: '最小值' }
                ]
            },
            markLine: {
                data: [{ type: 'average', name: '平均值' }]
            }
        },
        {
            name: '信安',
            type: 'line',
            data: [12, 14, 15, 15, 15, 15, 17, 16],
            markPoint: {
                data: [{ name: '最低', value: -2, xAxis: 1, yAxis: -1.5 }]
            },
            markLine: {
                data: [{ type: 'average', name: '平均值' }]
            }
        }
    ]
};

option && myChart.setOption(option);