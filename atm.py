from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt
from rich import box

console = Console()

balance = 10000
pin = 1122

console.clear()

console.print(Panel.fit(
"[bold cyan]🏦 YOGIBANK ATM 🏦[/bold cyan]\n"
"[white]SMART BANKING SYSTEM[/white]",
border_style="bright_blue",
padding=(1, 4)
))

entered_pin = IntPrompt.ask("[bold yellow]Enter your ATM PIN[/bold yellow]")

if entered_pin == pin:
    console.print("\n[bold green]✔ Login Successful![/bold green]\n")


while True:
    table = Table(
        title="💳 ATM SERVICES",
        box=box.ROUNDED,
        border_style="bright_blue",
        header_style="bold cyan"
    )

    table.add_column("Option", justify="center", style="yellow")
    table.add_column("Service", style="white")

    table.add_row("1", "💰 Check Balance")
    table.add_row("2", "📤 Withdraw Money")
    table.add_row("3", "📥 Deposit Money")
    table.add_row("4", "🔐 Change PIN")
    table.add_row("5", "🚪 Exit")

    console.print(table)

    choice = IntPrompt.ask("[bold cyan]Choose an option[/bold cyan]")

    if choice == 1:
        console.print(Panel(
            f"[bold green]Available Balance: ₹{balance:,}[/bold green]",
            title="ACCOUNT BALANCE",
            border_style="green"
        ))

    elif choice == 2:
        amount = IntPrompt.ask("[yellow]Enter withdrawal amount (₹)[/yellow]")

        if amount <= 0:
            console.print("[red]Amount must be greater than zero![/red]")
        elif amount <= balance:
            balance -= amount
            console.print(Panel(
                f"[green]Withdrawal Successful![/green]\n"
                f"Withdrawn: ₹{amount:,}\n"
                f"Remaining Balance: ₹{balance:,}",
                title="✔ TRANSACTION SUCCESS",
                border_style="green"
            ))
        else:
            console.print("[bold red]✘ Insufficient Balance![/bold red]")

    elif choice == 3:
        amount = IntPrompt.ask("[yellow]Enter deposit amount (₹)[/yellow]")

        if amount <= 0:
            console.print("[red]Amount must be greater than zero![/red]")
        else:
            balance += amount
            console.print(Panel(
                f"[green]Deposit Successful![/green]\n"
                f"Deposited: ₹{amount:,}\n"
                f"Updated Balance: ₹{balance:,}",
                title="✔ DEPOSIT SUCCESS",
                border_style="green"
            ))

    elif choice == 4:
        old_pin = IntPrompt.ask("[yellow]Enter your old PIN[/yellow]")

        if old_pin == pin:
            new_pin = IntPrompt.ask("[cyan]Enter new 4-digit PIN[/cyan]")

            if 1000 <= new_pin <= 9999 and new_pin != pin:
                pin = new_pin
                console.print("[bold green]✔ PIN changed successfully![/bold green]")
            else:
                console.print("[bold red]Enter a different 4-digit PIN![/bold red]")
        else:
            console.print("[bold red]✘ Incorrect old PIN![/bold red]")

    elif choice == 5:
        console.print(Panel.fit(
            "[bold cyan]Thank you for using YogiBank![/bold cyan]\n"
            "[green]Have a great day![/green]",
            border_style="bright_blue"
        ))
        break

    else:
        console.print("[bold red]Invalid Choice![/bold red]")


else:
    console.print(Panel("[bold red]✘ Incorrect PIN! Access Denied.[/bold red]",border_style="red"))
