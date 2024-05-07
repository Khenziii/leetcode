function longestCommonPrefix(strs: string[]): string {
    let finalString: string = "";

    /*
     * returns a list of chars for a given index from strs
     */
    function getIndex(index: number, strings: string[] = strs): string[] {
        let finalList: string[] = []

        for (const string of strings) {
            finalList.push(string[index]);
        }

        return finalList;
    }

    /*
     * returns true, if every element of the list is equal
     */
    function validateList(chars: string[]): boolean {
        let finalValue: boolean = true;
        let lastChar: string;

        for (const char of chars) {
            if (lastChar === undefined) {
                lastChar = char;
                continue;
            }

            if (char !== lastChar) {
                finalValue = false;
                break;
            }
        }

        return finalValue;
    }

    /*
     * returns the lenght of the shortest string in a string list
     */
    function getShortestLength(strings: string[] = strs): number {
        let finalNumber: number;

        for (const string of strings) {
            if (finalNumber === undefined) {
                finalNumber = string.length;
                continue;
            }

            if (string.length < finalNumber) finalNumber = string.length;
        }

        return finalNumber;
    }

    const length: number = getShortestLength();
    for (let i = 0; i < length; i++) {
        const list: string[] = getIndex(i);
        
        if (!validateList(list)) break;
        finalString += list[0]
    }

    return finalString;
};

