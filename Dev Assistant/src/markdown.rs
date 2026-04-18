use pulldown_cmark::{html, Options, Parser};

pub fn render_markdown(input: &str) -> String {
    let mut options = Options::empty();
    options.insert(Options::ENABLE_TABLES);
    options.insert(Options::ENABLE_STRIKETHROUGH);
    options.insert(Options::ENABLE_HEADING_ATTRIBUTES);
    let parser = Parser::new_ext(input, options);
    let mut html_output = String::new();
    html::push_html(&mut html_output, parser);
    html_output
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_heading() {
        let result = render_markdown("# Hello");
        assert!(result.contains("<h1>Hello</h1>"));
    }

    #[test]
    fn test_bold() {
        let result = render_markdown("**bold**");
        assert!(result.contains("<strong>bold</strong>"));
    }

    #[test]
    fn test_table() {
        let md = "| A | B |\n|---|---|\n| 1 | 2 |";
        let result = render_markdown(md);
        assert!(result.contains("<table>"));
        assert!(result.contains("<td>1</td>"));
    }

    #[test]
    fn test_empty_input() {
        let result = render_markdown("");
        assert_eq!(result, "");
    }
}
