function fish_prompt
		echo "test"
        set_color FB0 --bold
        echo "$USER"@(prompt_hostname)(set_color normal)(set_color 9AA) (date +%T)
        set_color normal
        echo '' (prompt_pwd) '> '
end
