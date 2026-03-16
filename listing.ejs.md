```{=html}
<div class="quarto-listing-container-custom">
<div class="list quarto-listing-custom" id="quarto-listing-listing">

<% for (const item of items) { %>
<%
  const d = new Date(item.date);
  const dateStr = d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
%>

<article class="plc-entry" <%- metadataAttrs(item) %>>

  <div class="plc-meta">
    <time class="plc-date listing-date" datetime="<%- item.date %>"><%- dateStr %></time>
    <% if (item['reading-time']) { %>
    <span class="plc-sep">·</span>
    <span class="plc-reading-time listing-reading-time"><%- item['reading-time'] %></span>
    <% } %>
  </div>

  <div class="plc-body">
    <% if (item.image) { %>
    <a href="<%- item.path %>" class="plc-image-link" tabindex="-1" aria-hidden="true">
      <img src="<%- item.image %>" alt="" class="plc-image" loading="lazy">
    </a>
    <% } %>

    <div class="plc-content">
      <h2 class="plc-title listing-title">
        <a href="<%- item.path %>" class="plc-title-link"><%- item.title %></a>
      </h2>

      <% if (item.description) { %>
      <p class="plc-description listing-description"><%- item.description %></p>
      <% } %>

      <% if (item.categories && item.categories.length > 0) { %>
      <div class="plc-categories">
        <% for (const cat of item.categories) { %>
        <a class="plc-category listing-category quarto-category"
           href="#"
           onclick="window.quartoListingCategory && window.quartoListingCategory('<%- cat %>'); return false;"><%- cat %></a>
        <% } %>
      </div>
      <% } %>
    </div>
  </div>

</article>

<% } %>

</div>
</div>
```
