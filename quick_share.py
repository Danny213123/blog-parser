from helper import grab_href

def quickshare (blog):
    css_style = """
<style>
/* Container for the quickshare buttons */
.quickshare-buttons {
  position: fixed;              /* Keeps the buttons in place during scroll */
  top: 50%;                     /* Positions the container halfway down the viewport */
  right: 0;                     /* Aligns the container to the right edge */
  transform: translateY(-50%);  /* Offsets the container to truly center it vertically */
  display: flex;                /* Uses flexbox for layout */
  flex-direction: column;       /* Stacks buttons vertically */
  gap: 10px;                    /* Adds space between each button */
  z-index: 1000;                /* Ensures the buttons appear above other content */
}

/* Styling for each quickshare button (assumed to be an anchor/link) */
.quickshare-buttons a {
  background-color: #fff;       /* White background for minimalism */
  color: #000;                  /* Black text */
  border: 1px solid #000;       /* Black border for definition */
  padding: 8px 12px;            /* Padding for a clickable area */
  text-decoration: none;        /* Removes underline from links */
  font-size: 14px;              /* Readable, small font size */
  transition: background-color 0.3s, color 0.3s;  /* Smooth color transitions on hover */
}

/* Hover state to invert colors for visual feedback */
.quickshare-buttons a:hover {
  background-color: #000;       /* Inverts to black background on hover */
  color: #fff;                  /* Inverts text to white */
}
</style>

<div class="quickshare-buttons">
  <!-- LinkedIn Share Button -->
  <a href="https://www.linkedin.com/shareArticle?mini=true&amp;url={URL}&amp;title={TITLE}" 
     target="_blank" 
     rel="noopener noreferrer">
    LinkedIn
  </a>
  
  <!-- Reddit Share Button -->
  <a href="https://www.reddit.com/submit?url={URL}&amp;title={TITLE}" 
     target="_blank" 
     rel="noopener noreferrer">
    Reddit
  </a>
  
  <!-- Twitter Share Button -->
  <a href="https://twitter.com/intent/tweet?url={URL}&amp;text={TEXT}" 
     target="_blank" 
     rel="noopener noreferrer">
    Twitter
  </a>
</div>
"""

    url = f"http://rocm.blogs.amd.com{grab_href(blog)[1:]}"

    title = blog.blog_title if hasattr(blog, "blog_title") else "No Title"

    text = blog.blog_description if hasattr(blog, "blog_description") else "No Description"

    css_style = css_style.replace("{URL}", url).replace("{TITLE}", title).replace("{TEXT}", text)

    return css_style
