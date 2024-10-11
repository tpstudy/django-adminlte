// landing.js

document.addEventListener('DOMContentLoaded', function() {
    // 添加滚动动画效果
    window.addEventListener('scroll', function() {
        var featureSections = document.querySelectorAll('.feature-section');
        featureSections.forEach(function(section) {
            var bottomOfObject = section.offsetTop + section.offsetHeight;
            var bottomOfWindow = window.scrollY + window.innerHeight;
            if (bottomOfWindow > bottomOfObject) {
                section.style.opacity = '1';
                section.style.transition = 'opacity 500ms';
            }
        });
    });
});
