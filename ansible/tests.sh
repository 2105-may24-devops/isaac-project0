python3 p0.py output.css -f input.txt
if cmp output.css test/output-txt.css; then
	echo 'Plaintext test passed'
else
	echo 'Plaintext test failed'
	exit 1
fi

python3 p0.py output.css -x input.xml
if cmp output.css test/output-xml.css; then
	echo 'Basic XML test passed'
else
	echo 'Basic XML test failed'
	exit 1
fi

python3 p0.py output.css -x complicated.xml
if cmp output.css test/output-complicated.css; then
	echo 'Complex XML test passed'
else
	echo 'Complex XML test failed'
	exit 1
fi

cat input.txt | python3 p0.py output.css -i > /dev/null
# Direct to /dev/null so we don't clutter our screen
# with the syntax reminder that gets printed in an
# interactive session
if cmp output.css test/output-interactive.css; then
	echo 'Interactive test passed'
else
	echo 'Interactive test failed'
	exit 1
fi

python3 p0.py output.css -c -p font-size 12px
if cmp output.css test/output-cli.css; then
	echo 'CLI test passed'
else
	echo 'CLI test failed'
	exit 1
fi

