//! Crop/trim/stack primitives for exhibit extraction.

use image::{Rgb, RgbImage};

const WHITE_THRESHOLD: u8 = 245;
const PAD_PX: u32 = 8;

/// Crop by [left, top, right, bottom] page fractions.
pub fn crop_pct(img: &RgbImage, box_pct: [f64; 4]) -> RgbImage {
    let (w, h) = img.dimensions();
    let x0 = (w as f64 * box_pct[0]) as u32;
    let y0 = (h as f64 * box_pct[1]) as u32;
    let x1 = ((w as f64 * box_pct[2]) as u32).min(w);
    let y1 = ((h as f64 * box_pct[3]) as u32).min(h);
    image::imageops::crop_imm(img, x0, y0, x1 - x0, y1 - y0).to_image()
}

/// Trim surrounding near-white border, keeping PAD_PX padding.
pub fn trim_white(img: &RgbImage) -> RgbImage {
    let (w, h) = img.dimensions();
    let is_ink = |p: &Rgb<u8>| p.0.iter().any(|&c| c < WHITE_THRESHOLD);
    let (mut x0, mut y0, mut x1, mut y1) = (w, h, 0u32, 0u32);
    for (x, y, p) in img.enumerate_pixels() {
        if is_ink(p) {
            x0 = x0.min(x);
            y0 = y0.min(y);
            x1 = x1.max(x);
            y1 = y1.max(y);
        }
    }
    if x0 > x1 {
        return img.clone(); // fully white: nothing to trim
    }
    let x0 = x0.saturating_sub(PAD_PX);
    let y0 = y0.saturating_sub(PAD_PX);
    let x1 = (x1 + PAD_PX + 1).min(w);
    let y1 = (y1 + PAD_PX + 1).min(h);
    image::imageops::crop_imm(img, x0, y0, x1 - x0, y1 - y0).to_image()
}

/// Stack images vertically, centered on white, width = widest part.
pub fn stack(parts: &[RgbImage]) -> RgbImage {
    let w = parts.iter().map(|p| p.width()).max().unwrap_or(1);
    let h: u32 = parts.iter().map(|p| p.height()).sum();
    let mut out = RgbImage::from_pixel(w, h.max(1), Rgb([255, 255, 255]));
    let mut y = 0i64;
    for p in parts {
        image::imageops::overlay(&mut out, p, ((w - p.width()) / 2) as i64, y);
        y += p.height() as i64;
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    fn white(w: u32, h: u32) -> RgbImage {
        RgbImage::from_pixel(w, h, Rgb([255, 255, 255]))
    }

    #[test]
    fn crop_pct_halves() {
        let img = white(100, 200);
        let c = crop_pct(&img, [0.25, 0.10, 0.75, 0.60]);
        assert_eq!(c.dimensions(), (50, 100));
    }

    #[test]
    fn trim_white_finds_ink_bbox() {
        let mut img = white(100, 100);
        img.put_pixel(40, 50, Rgb([0, 0, 0]));
        img.put_pixel(60, 55, Rgb([0, 0, 0]));
        let t = trim_white(&img);
        // ink bbox 21x6 plus 8px pad each side
        assert_eq!(t.dimensions(), (21 + 16, 6 + 16));
    }

    #[test]
    fn trim_all_white_is_identity() {
        let img = white(30, 30);
        assert_eq!(trim_white(&img).dimensions(), (30, 30));
    }

    #[test]
    fn stack_centers_and_sums_heights() {
        let s = stack(&[white(40, 10), white(60, 20)]);
        assert_eq!(s.dimensions(), (60, 30));
    }
}
