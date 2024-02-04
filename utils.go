package main

import (
	"crypto/rand"
	"fmt"
	"github.com/NoahOnFyre/gengine/utils"
	"os/exec"
)

var (
	state = "No State"
)

func RandomBytes(size int) (blk []byte, err error) {
	blk = make([]byte, size)
	_, err = rand.Read(blk)
	return
}

func MultiString(char string, repeat int) string {
	final := ""
	for i := 0; i < repeat; i++ {
		final += char
	}
	return final
}

func SetState(msg string) {
	state = msg
	utils.SetTitle("FyUTILS " + version + " - " + username + "@" + device + " - " + state)
}

func PowerShellRun(command string) {
	cmd := exec.Command("cmd.exe", "/c", "powershell.exe -nologo -noprofile")
	stdin, err := cmd.StdinPipe()
	if err != nil {
		Error("Failed to connect to PowerShell session!")
		return
	}
	bytesWritten, err := fmt.Fprintln(stdin, command)
	Print(fmt.Sprint(bytesWritten), "bytes written to pipe.")
	if err != nil {
		Error("Failed to run PowerShell command.")
		return
	}
	err = stdin.Close()
	if err != nil {
		Error("Failed to close pipe..")
		return
	}
	out, err := cmd.CombinedOutput()
	if err != nil {
		Error(err.Error())
	}
	Print(string(out))
}
