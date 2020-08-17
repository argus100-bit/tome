from tkinter import *
import random


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width=1280, height=700)
        self.root.minsize(width=1280, height=700)
        self.root.title("Billing Software")

        # ====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        # For Generating Random Bill Numbers
        x = random.randint(1000, 9999)
        self.c_bill_no = StringVar()
        # Seting Value to variable
        self.c_bill_no.set(str(x))

        self.spaghetti = IntVar()
        self.fried_rice = IntVar()
        self.buff_momo = IntVar()
        self.pi_lasagna = IntVar()
        self.beast_pizza = IntVar()
        self.fish = IntVar()
        self.daal = IntVar()
        self.parautha = IntVar()
        self.bread = IntVar()
        self.steak = IntVar()
        self.wine = IntVar()
        self.coke = IntVar()
        self.brooth = IntVar()
        self.juice = IntVar()
        self.vermouth = IntVar()
        self.starving_total = StringVar()
        self.total_casual = StringVar()
        self.total_liquify = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()

        # ===================================
        bg_color = "seagreen3"
        fg_color = "black"
        lbl_color = 'black'
        # Title of App
        title = Label(self.root, text="Argus Eatery Billing", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
                      font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

        # ==========Customers Frame==========#
        F1 = LabelFrame(text="Customer Details", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                        relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        # ===============Customer Name===========#
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        # =================Customer Phone==============#
        cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20)
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # ====================Customer Bill No==================#
        cbill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # ====================Bill Search Button===============#
        bill_btn = Button(F1, text="Enter", bd=7, relief=GROOVE, font=("times new roman", 12, "bold"), bg=bg_color,
                          fg=fg_color)
        bill_btn.grid(row=0, column=6, ipady=5, padx=60, ipadx=19, pady=5)

        # ==================1st frame=====================#
        F2 = LabelFrame(self.root, text='Starving', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=5, y=180, width=325, height=380)

        # ===========Frame Content
        bath_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Spagetti")
        bath_lbl.grid(row=0, column=0, padx=10, pady=20)
        bath_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.spaghetti)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======Fried Rice
        fry_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Fried Rice")
        fry_lbl.grid(row=1, column=0, padx=10, pady=20)
        fry_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.fried_rice)
        fry_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # ========Buff Momo
        buff_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Buff Momo")
        buff_lbl.grid(row=2, column=0, padx=10, pady=20)
        buff_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.buff_momo)
        buff_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========Pi Lasagna
        las_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Pi Lasagna")
        las_lbl.grid(row=3, column=0, padx=10, pady=20)
        las_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.pi_lasagna)
        las_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============Beast Pizza
        lot_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Beast Pizza")
        lot_lbl.grid(row=4, column=0, padx=10, pady=20)
        lot_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.beast_pizza)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ==================2nd Frame=====================#
        F2 = LabelFrame(self.root, text='Casual Eating', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=330, y=180, width=325, height=380)

        # ===========Frame Content
        ric_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Fish")
        ric_lbl.grid(row=0, column=0, padx=10, pady=20)
        ric_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.fish)
        ric_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        oil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Parautha")
        oil_lbl.grid(row=1, column=0, padx=10, pady=20)
        oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.parautha)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        daal_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Daal")
        daal_lbl.grid(row=2, column=0, padx=10, pady=20)
        daal_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.daal)
        daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========
        whe_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Bread")
        whe_lbl.grid(row=3, column=0, padx=10, pady=20)
        whe_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.bread)
        whe_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============
        sug_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Steak")
        sug_lbl.grid(row=4, column=0, padx=10, pady=20)
        sug_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.steak)
        sug_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ==================Other Stuff=====================#

        F2 = LabelFrame(self.root, text='Liquify', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=655, y=180, width=325, height=380)

        # ===========Frame Content
        maz_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Wine")
        maz_lbl.grid(row=0, column=0, padx=10, pady=20)
        maz_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.wine)
        maz_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        cola_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Coke")
        cola_lbl.grid(row=1, column=0, padx=10, pady=20)
        cola_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.coke)
        cola_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        fro_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Brooth")
        fro_lbl.grid(row=2, column=0, padx=10, pady=20)
        fro_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.brooth)
        fro_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========
        cold_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Juices")
        cold_lbl.grid(row=3, column=0, padx=10, pady=20)
        cold_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.juice)
        cold_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============
        bis_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Vermouth")
        bis_lbl.grid(row=4, column=0, padx=10, pady=20)
        bis_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.vermouth)
        bis_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ===================Bill Aera================#
        F3 = Label(self.root, bd=10, relief=GROOVE)
        F3.place(x=960, y=180, width=325, height=380)
        # ===========
        bill_title = Label(F3, text="Bill Area", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        # ============
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ===========Buttons Frame=============#
        F4 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F4.place(x=0, y=560, relwidth=1, height=145)

        # ===================
        cosm_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Starving")
        cosm_lbl.grid(row=0, column=0, padx=10, pady=0)
        cosm_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.starving_total)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        # ===================
        gro_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Casual")
        gro_lbl.grid(row=1, column=0, padx=10, pady=5)
        gro_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_casual)
        gro_en.grid(row=1, column=1, ipady=2, ipadx=5)

        # ================
        oth_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Liquify")
        oth_lbl.grid(row=2, column=0, padx=10, pady=5)
        oth_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_liquify)
        oth_en.grid(row=2, column=1, ipady=2, ipadx=5)

        # ================
        cosmt_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Starving Tax")
        cosmt_lbl.grid(row=0, column=2, padx=30, pady=0)
        cosmt_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_cos)
        cosmt_en.grid(row=0, column=3, ipady=2, ipadx=5)

        # =================
        grot_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Casual Tax")
        grot_lbl.grid(row=1, column=2, padx=30, pady=5)
        grot_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_groc)
        grot_en.grid(row=1, column=3, ipady=2, ipadx=5)

        # ==================
        otht_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Liquify Tax")
        otht_lbl.grid(row=2, column=2, padx=10, pady=5)
        otht_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_other)
        otht_en.grid(row=2, column=3, ipady=2, ipadx=5)

        # ====================
        total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.total)
        total_btn.grid(row=1, column=4, ipadx=20, padx=30)

        # ========================
        genbill_btn = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=5, ipadx=20)

        # ====================
        clear_btn = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=1, column=6, ipadx=20, padx=30)

        # ======================
        exit_btn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=20)

    # Function to get total prices
    def total(self):
        # =================Total starving Prices
        self.starving_total_prices = (
                (self.spaghetti.get() * 40) +
                (self.fried_rice.get() * 140) +
                (self.buff_momo.get() * 240) +
                (self.pi_lasagna.get() * 340) +
                (self.beast_pizza.get() * 260)
        )
        self.starving_total.set("Rs. " + str(self.starving_total_prices))
        self.tax_cos.set("Rs. " + str(round(self.starving_total_prices * 0.05)))
        # ====================Total casual prices
        self.total_casual_prices = (
                (self.bread.get() * 100) +
                (self.parautha.get() * 180) +
                (self.daal.get() * 80) +
                (self.fish.get() * 80) +
                (self.steak.get() * 170)

        )
        self.total_casual.set("Rs. " + str(self.total_casual_prices))
        self.tax_groc.set("Rs. " + str(round(self.total_casual_prices * 0.05)))
        # ======================Total liquify Prices
        self.total_liquify_prices = (
                (self.wine.get() * 20) +
                (self.brooth.get() * 50) +
                (self.coke.get() * 60) +
                (self.juice.get() * 20) +
                (self.vermouth.get() * 20)
        )
        self.total_liquify.set("Rs. " + str(self.total_liquify_prices))
        self.tax_other.set("Rs. " + str(round(self.total_liquify_prices * 0.05)))

    # Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "       Welcome To Argus Eatery\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n===================================")

    # Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0', END)

    # Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.spaghetti.get() != 0:
            self.txt.insert(END, f"\nSpaghetti         {self.spaghetti.get()}           {self.spaghetti.get() * 40}")
        if self.fried_rice.get() != 0:
            self.txt.insert(END, f"\nFried Rice        {self.fried_rice.get()}           {self.fried_rice.get() * 140}")
        if self.buff_momo.get() != 0:
            self.txt.insert(END, f"\nBuff Momo         {self.buff_momo.get()}           {self.buff_momo.get() * 240}")
        if self.pi_lasagna.get() != 0:
            self.txt.insert(END, f"\nPi Lasagna        {self.pi_lasagna.get()}           {self.pi_lasagna.get() * 340}")
        if self.beast_pizza.get() != 0:
            self.txt.insert(END,
                            f"\nBeast Pizza       {self.beast_pizza.get()}           {self.beast_pizza.get() * 260}")
        if self.bread.get() != 0:
            self.txt.insert(END, f"\nBread             {self.bread.get()}           {self.bread.get() * 100}")
        if self.parautha.get() != 0:
            self.txt.insert(END, f"\nParautha          {self.parautha.get()}           {self.parautha.get() * 180}")
        if self.daal.get() != 0:
            self.txt.insert(END, f"\nDaal              {self.daal.get()}           {self.daal.get() * 80}")
        if self.fish.get() != 0:
            self.txt.insert(END, f"\nFish              {self.fish.get()}           {self.fish.get() * 80}")
        if self.steak.get() != 0:
            self.txt.insert(END, f"\nSteak             {self.steak.get()}           {self.steak.get() * 170}")
        if self.wine.get() != 0:
            self.txt.insert(END, f"\nWine              {self.wine.get()}           {self.wine.get() * 20}")
        if self.brooth.get() != 0:
            self.txt.insert(END, f"\nBrooth            {self.brooth.get()}           {self.brooth.get() * 50}")
        if self.coke.get() != 0:
            self.txt.insert(END, f"\nCoke              {self.coke.get()}           {self.coke.get() * 60}")
        if self.juice.get() != 0:
            self.txt.insert(END, f"\nJuice             {self.juice.get()}           {self.juice.get() * 20}")
        if self.vermouth.get() != 0:
            self.txt.insert(END, f"\nVermouth          {self.vermouth.get()}           {self.vermouth.get() * 20}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n                      Total : {self.starving_total_prices + self.total_casual_prices + self.total_liquify_prices + self.starving_total_prices * 0.05 + self.total_casual_prices * 0.05 + self.total_liquify_prices * 0.05}")

    # Function to exit
    def exit(self):
        self.root.destroy()

    # Function To Clear All Fields


root = Tk()
object = Bill_App(root)
root.mainloop()


