# Changelog: JavaScript to HTMX Migration

## Summary
Replaced client-side JavaScript filtering with server-side HTMX implementation for the mango project.

## Changes Made

1. **Added HTMX Library**
   - Added HTMX script to base.html template

2. **Updated ProjectListView**
   - Modified to handle filter parameters (`all`, `pest`, `disease`) 
   - Added HTMX-specific response logic using content negotiation
   - Filter application now happens on the server

3. **Created Partial Template**
   - New `partials/item_grid.html` for filtered content
   - Supports HTMX targeted updates

4. **Updated UI Elements**
   - Filter buttons now use HTMX attributes instead of data attributes
   - Homepage links now use query parameters instead of hash fragments
   - Removed sessionStorage usage

5. **Simplified JavaScript**
   - Removed all custom JavaScript code (~90 lines)
   - Replaced with empty file containing only a documentation comment

## How It Works

### Before: Client-Side Filtering
```
User clicks filter button → JavaScript handles click → JavaScript hides/shows elements → UI updates
```

### After: Server-Side Filtering with HTMX
```
User clicks filter button → HTMX sends request → Server filters data → Server returns partial HTML → HTMX updates target element
```

### Key HTMX Attributes Used
- `hx-get`: Makes GET request to URL when triggered
- `hx-target`: Specifies which element to update with response
- `hx-trigger`: Defines event that triggers the request (click)
- `hx-swap`: Determines how content is swapped (innerHTML)
- `hx-push-url`: Updates browser URL for history/bookmarking

### Filter Parameter Flow
1. User clicks "Pests Only" button
2. HTMX sends GET request to `/projects/?filter=pest`  
3. View filters items to only show pests
4. View returns partial HTML with only pest items
5. HTMX updates just the items container with new content
6. URL changes to reflect current filter

### Benefits
- Reduced JavaScript code (90 lines → 0 lines)
- More maintainable Django-centric approach
- Better accessibility and SEO
- Proper browser history support
- Faster initial page load
- Same UX with less code