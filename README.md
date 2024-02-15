# What is this?

This is a plugin for the [Cheshire Cat Project](https://github.com/pieroit/cheshire-cat), which allows you to put URL content directly in prompt

# Usage

After plugin installation you can insert in your prompt a palceholder like this:

{{url}}

The plugin automatically get the content of the url and substitute the placeholder with the URL content.

The plugina utomatically remove from ulr content this HTML tags:

["script", "noscript", "link", "style", "head", "footer", "header", "nav"]

# Settings

On the plugin settings you can set "Remove HTML Tags": this setting strip all html tags from the url content before insert it into the prompt. If this settings is disabled URL content contains original html tags.

# Example

"Give me the summary of the following text {{https://cheshire-cat-ai.github.io/docs/plugins-registry/publishing-plugin/}}"
