function gps_line()
    print("Line " .. vim.fn.line('.') .. "/" .. vim.api.nvim_buf_line_count(0))
end
