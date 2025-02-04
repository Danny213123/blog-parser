from helper import grab_href

def quickshare (blog):
    css_style = """
<style>
/* Fixed/sticky icon bar (vertically aligned 50% from the top of the screen) */
.icon-bar {
  position: fixed;
  top: 50%;
  transform: translateY(-50%);
}

/* Style the icon bar links */
.icon-bar a {
  display: block;
  text-align: center;
  padding: 16px;
  transition: all 0.3s ease;
  color: white;
  font-size: 20px;
}

/* Style the social media icons with color, if you want */
.icon-bar a:hover {
  background-color: #000;
}

.facebook {
  background: #3B5998;
  color: white;
}

.twitter {
  background: #55ACEE;
  color: white;
}

.google {
  background: #dd4b39;
  color: white;
}

.linkedin {
  background: #007bb5;
  color: white;
}

.youtube {
  background: #bb0000;
  color: white;
}
</style>

<!-- The social media icon bar -->
<div class="icon-bar">
  <a href="#" class="facebook"><i class="fa fa-facebook"></i></a>
  <a href="https://twitter.com/intent/tweet?url={URL}&amp;text={TEXT}" class="twitter"><i class="fa fa-twitter"></i></a>
  <a href="https://www.reddit.com/submit?url={URL}&amp;title={TITLE}" class="google"><i class="fa fa-google"></i></a>
  <a href="https://www.linkedin.com/shareArticle?mini=true&amp;url={URL}&amp;title={TITLE}" class="linkedin"><i class="fa fa-linkedin"></i></a>
  <a href="#" class="youtube"><i class="fa fa-youtube"></i></a>
</div>
"""

    url = f"http://rocm.blogs.amd.com{grab_href(blog)[1:]}"

    title = blog.blog_title if hasattr(blog, "blog_title") else "No Title"

    if hasattr(blog, "myst"):

        print(blog.myst.get("html_meta").get("description lang=en"))
        description = (
            blog.myst.get("html_meta").get("description lang=en")
            if blog.myst.get("html_meta").get("description lang=en")
            else "No Description"
        )

    css_style = css_style.replace("{URL}", url).replace("{TITLE}", title).replace("{TEXT}", description)

    return css_style
