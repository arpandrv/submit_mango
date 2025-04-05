/**
 * Mango Surveillance Website - Main JavaScript
 */

// Execute when DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    // Initialize filter functionality for project list page
    initializeProjectFilters();
    
    // Handle the pest filter link from homepage
    const pestFilterLinks = document.querySelectorAll('.pest-filter-link');
    pestFilterLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Store in sessionStorage that we want to filter by pest
            sessionStorage.setItem('filterType', 'pest');
        });
    });
    
    // Handle the disease filter link from homepage
    const diseaseFilterLinks = document.querySelectorAll('.disease-filter-link');
    diseaseFilterLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Store in sessionStorage that we want to filter by disease
            sessionStorage.setItem('filterType', 'disease');
        });
    });
    
    // Check if we should auto-filter on the projects page
    if (window.location.pathname.includes('/projects/')) {
        const filterType = sessionStorage.getItem('filterType');
        if (filterType) {
            // Find and click the relevant filter button
            const filterButton = document.querySelector(`[data-filter="${filterType}"]`);
            if (filterButton) {
                filterButton.click();
            }
            // Clear the stored filter type
            sessionStorage.removeItem('filterType');
        }
    }
    
    // If the URL has a hash for filtering
    if (window.location.hash) {
        const hashId = window.location.hash.substring(1); // Remove the # character
        const filterElement = document.getElementById(hashId);
        if (filterElement && filterElement.hasAttribute('data-filter')) {
            // Simulate a click on the filter button
            filterElement.click();
            
            // Scroll to the element
            setTimeout(function() {
                filterElement.scrollIntoView({ behavior: 'smooth' });
            }, 200);
        }
    }
});

/**
 * Initialize filter functionality for the project list page
 */
function initializeProjectFilters() {
    // Get filter buttons and item cards
    const filterButtons = document.querySelectorAll('[data-filter]');
    const itemCards = document.querySelectorAll('.item-card');
    
    // If no filter buttons found, we're not on the projects page
    if (filterButtons.length === 0) return;
    
    // Add click event listeners to filter buttons
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Get filter value
            const filterValue = this.getAttribute('data-filter');
            
            // Show/hide cards based on filter value
            itemCards.forEach(card => {
                if (filterValue === 'all' || card.getAttribute('data-type') === filterValue) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}