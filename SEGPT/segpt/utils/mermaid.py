from pathlib import Path


def mermaid_to_file(mermaid_code, output_file_without_suffix, width=2048, height=2048) -> int:
    """suffix: png/svg/pdf

    :param mermaid_code: mermaid code
    :param output_file_without_suffix: output filename
    :param width:
    :param height:
    :return: 0 if succed, -1 if failed
    """
    # Write the Mermaid code to a temporary file
    tmp = Path(f'{output_file_without_suffix}.mmd')
    tmp.write_text(mermaid_code, encoding='utf-8')

    # if check_cmd_exists('mmdc') != 0:
    #     logger.warning(
    #         "RUN `npm install -g @mermaid-js/mermaid-cli` to install mmdc")
    #     return -1

    # for suffix in ['pdf', 'svg', 'png']:
    #     output_file = f'{output_file_without_suffix}.{suffix}'
    #     # Call the `mmdc` command to convert the Mermaid code to a PNG
    #     logger.info(f"Generating {output_file}..")
    #     if IS_DOCKER == 'true':
    #         subprocess.run(['mmdc', '-p', '/app/metagpt/puppeteer-config.json', '-i',
    #                       str(tmp), '-o', output_file, '-w', str(width), '-H', str(height)])
    #     else:
    #         if CONFIG.puppeteer_config:
    #             subprocess.run([CONFIG.mmdc,'-p',CONFIG.puppeteer_config, '-i', str(tmp), '-o',
    #                       output_file, '-w', str(width), '-H', str(height)])
    #         else:
    #             subprocess.run( [CONFIG.mmdc, '-i', str(tmp), '-o',
    #                       output_file, '-w', str(width), '-H', str(height)])
    return 0