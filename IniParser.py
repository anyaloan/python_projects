class IniParser:
    def __init__(self, file):
        if file.endswith(".ini"):
            self.file = file
        else:
            print("Unsupported format")

    def read(self):
        with open(self.file, "r") as mf:
            cont = mf.read()
        return cont

    @staticmethod
    def parser(cont):
        md = {}
        nd = {}

        ml = cont.strip().split("[")
        for section in ml[1:]:
            raw = section.strip().split("\n")
            for el in raw[1:]:
                if raw[0] != "DEFAULTS]":
                    if not el.strip().startswith(";") or \
                            el.strip().startswith("#"):
                        key, value = el.split(" = ")
                        md[raw[0][:-1]] = nd
                        nd[key] = value
            nd = {}
        return md


    def __getitem__(self, section):
        cont = self.read()
        cont_dict = self.parser(cont)
        if section == "Sections":
            ans = list(cont_dict.keys())
            ans.remove("DEFAULTS")
            return f"Sections: {ans}"
        elif section in cont_dict:
            ans = cont_dict[section]
            n_str = ''
            for key, value in ans.items():
                m_str = f'{key}: {value}'
                n_str = f'{n_str} \n{m_str}'
            return n_str
        elif isinstance(section, tuple):
            if len(section) == 2:
                sect, name = section
                ans = cont_dict[sect]
                return f"{ans[name]}"
            else:
                return "Not found"
        else:
            return "Not found"

    def __repr__(self):
        cont = self.read()
        cont_dict = self.parser(cont)
        ans = ''
        for section, raw in cont_dict.items():
            m_str = f"[{section}]\n"
            for key, val in raw.items():
                n_str = f'{key}: {val}\n'
                m_str = f'{m_str}{n_str}'
            ans = f"{ans}{m_str}\n"
        return ans
