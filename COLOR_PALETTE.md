# 🎨 YellowCert Color Palette

Updated color scheme for medical certificate detection with **high visual contrast** for easy class identification.

## Color Assignments

| Class | Color | Hex Code | Visual | Meaning |
|-------|-------|----------|--------|---------|
| **Cholera** | Teal | `#26A69A` | 🟦 | Water/hygiene related |
| **COVID-19** | Bright Blue | `#2196F3` | 🔵 | Medical blue |
| **Date** | Purple | `#9C27B0` | 🟣 | Administrative/documentation |
| **Flu** | Green | `#4CAF50` | 🟢 | Health/wellness |
| **Logo** | Navy Blue | `#1565C0` | 🔷 | Professional/official |
| **Meningococcal** | Pink/Magenta | `#E91E63` | 🔴 | Alert/important |
| **Signature** | Indigo | `#5E35B1` | 🟪 | Authority/validation |
| **Yellow Fever** | Orange/Amber | `#FF9800` | 🟠 | Yellow fever specific |

## Color Distribution

### Color Spectrum Coverage:
- **Cool Colors** (Blues/Teals): Cholera, COVID, Logo
- **Purple Range**: Date, Signature
- **Warm Colors**: Flu (Green), Yellow Fever (Orange)
- **Alert Colors**: Meningococcal (Pink)

### Visual Separation:
✅ **High Contrast** - Each color is easily distinguishable
✅ **Professional** - Medical-appropriate color palette
✅ **Accessible** - Good visibility on white backgrounds
✅ **Meaningful** - Colors relate to their medical context

## Before vs After

### Before (All Similar Teal):
```
Cholera:    #26A69A (Teal)
COVID:      #00ACC1 (Cyan - too close to teal)
Date:       #0097A7 (Teal - too close)
Flu:        #00897B (Teal - too close)
Logo:       #00796B (Dark Teal - too close)
Meningo:    #0288D1 (Light Blue - somewhat distinct)
Signature:  #00695C (Dark Teal - too close)
YellowFever:#FFA726 (Orange - distinct)
```
**Problem:** 6 out of 8 colors were similar teal/cyan shades!

### After (Diverse Spectrum):
```
Cholera:    #26A69A (Teal)
COVID:      #2196F3 (Bright Blue) ✨
Date:       #9C27B0 (Purple) ✨
Flu:        #4CAF50 (Green) ✨
Logo:       #1565C0 (Navy) ✨
Meningo:    #E91E63 (Pink) ✨
Signature:  #5E35B1 (Indigo) ✨
YellowFever:#FF9800 (Orange)
```
**Solution:** 8 clearly distinct colors across the spectrum!

## Usage

These colors are automatically applied to:
- ✅ Bounding boxes on detected images
- ✅ Detection list items (left border)
- ✅ Color indicators in the results panel
- ✅ Confidence badges

## Color Accessibility

All colors have been chosen to ensure:
- High contrast against white backgrounds
- Distinguishable by most users (including those with common color vision deficiencies)
- Professional medical aesthetic
- Clear visual hierarchy

## Customization

To change colors, edit `/frontend/src/App.js`:

```javascript
const CLASS_COLORS = {
  'cholera': '#26A69A',      // Your custom color
  'covid': '#2196F3',        // Your custom color
  // ... etc
};
```

Then restart the frontend:
```bash
cd frontend
npm start
```

---

**Updated:** 2025-01-19
**Version:** 2.0 - High Contrast Medical Palette
