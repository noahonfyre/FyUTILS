package main

import (
	"crypto/rand"
	"strings"
	"syscall"
	"unsafe"

	"github.com/hugolgst/rich-go/client"
)

func ValueOf(thing string, err error) string {
	if err != nil {
		Print(Prefix(0) + "An error occurred: " + err.Error())
	}
	return thing
}

func RandomBytes(size int) (blk []byte, err error) {
	blk = make([]byte, size)
	_, err = rand.Read(blk)
	return
}

func RemoveElement(slice []string, index int) []string {
	return append(slice[:index], slice[index+1:]...)
}

func SetTitle() {
	var title string = "FyUTILS " + version + " - " + username + "@" + device + " - " + state
	handle, err := syscall.LoadLibrary("Kernel32.dll")
	if err != nil {
		return
	}
	defer syscall.FreeLibrary(handle)
	proc, err := syscall.GetProcAddress(handle, "SetConsoleTitleW")
	if err != nil {
		return
	}
	syscall.Syscall(proc, 1, uintptr(unsafe.Pointer(syscall.StringToUTF16Ptr(title))), 0, 0)
}

func UpdateRPC() {
	go func() {
		if config.EnableDiscordRPC && rpc_active {
			err := client.SetActivity(client.Activity{
				Details:    "FyUTILS " + version,
				State:      GetState(),
				LargeImage: "placeholder",
				SmallImage: "placeholder",
				LargeText:  "FyUTILS " + version,
				SmallText:  username + "@" + device,
				Timestamps: &client.Timestamps{
					Start: &start_time,
				},
			})

			if err != nil {
				Print(Prefix(2) + "Failed to update RPC!")
				return
			}
		}
	}()
}

func StopRPC() {
	if config.EnableDiscordRPC && rpc_active {
		client.Logout()
	}
}

func SetState(str string) {
	state = str
	SetTitle()
	UpdateRPC()
}

func GetState() string {
	if state == "" {
		return "No current state!"
	} else {
		return state
	}
}

func Input(msg string) string {
	PrintR(msg)
	scanner.Scan()
	return scanner.Text()
}

func RInput(msg string) string {
	PrintR(msg)
	scanner.Scan()
	return scanner.Text()
}

func CommandInput() (string, []string) {
	commandLine := Gray + "┌───[" + Blue + username + Gray + "@" + Reset + device + Gray + "]\n" + Gray + "└─> " + Reset

	userInput := Input(commandLine)
	splitted := strings.Split(userInput, " ")
	command := splitted[0]
	args := RemoveElement(splitted, 0)
	return command, args
}