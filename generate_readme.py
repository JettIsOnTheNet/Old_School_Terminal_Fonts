import os
from fontpreview import FontBanner

patched_dir_str = 'patched'
previews_dir_str = 'previews'
header_file_str = 'HEADER.md'
readme_file_str = 'README.md'

def generate_preview_images(patched_dir_str, previews_dir_str, ttf_files_lst):

    preview_str = '''
  for (var i = 0; i < specs.length; ++i) {
          var gutterClass = __specs[i];
          var gElt = gutters.appendChild(
              elt(
                  "div",
                  null,
                  "CodeMirror-gutter " + gutterClass
                  )
              );
          if (gutterClass == "CodeMirror-linenumbers") {
              cm.display.lineGutter = gElt;
              gElt.style.width = (cm.display.lineNumWidth || 1) + "px";
              }
          '''

    for ttf_file in ttf_files_lst:
        fb = FontBanner(
            os.path.join(patched_dir_str, ttf_file), 
            (800, 600),
            bg_color=(000, 000, 000),
            fg_color=(141, 194, 137),
            font_size=40,
            mode='paragraph',
            )
        fb.font_text = preview_str 
        fb.set_text_position('ltop')
        fb.draw()

        fb.save(os.path.join(previews_dir_str, ttf_file + '.png'))

def generate_readme(patched_dir_str, previews_dir_str, ttf_files_lst, header_file_str, readme_file_str):

    header_file = open(header_file_str, 'r')
    header_body_str = header_file.read()
    header_file.close()

    readme_body = ''

    for ttf_file in ttf_files_lst:
        readme_body += '### [' + ttf_file +'](' + patched_dir_str + '/' + ttf_file + ')\n![' + ttf_file + '](' + previews_dir_str + '/' + ttf_file + '.png)\n'
    
    readme_file = open(readme_file_str, 'w')
    readme_file.write(header_body_str + readme_body)

if __name__ == '__main__':
    ttf_files_lst = [f for f in os.listdir(patched_dir_str) if f.endswith('.ttf')]
    generate_preview_images(patched_dir_str, previews_dir_str, ttf_files_lst)
    generate_readme(patched_dir_str, previews_dir_str, ttf_files_lst, header_file_str, readme_file_str)

