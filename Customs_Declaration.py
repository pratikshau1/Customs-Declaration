class CustomsDeclaration:
    def __init__(self, declaration_id, traveler_name, items, compliance_status):
        self.declaration_id = declaration_id
        self.traveler_name = traveler_name
        self.items = items
        self.compliance_status = compliance_status


class CustomsDeclarationSystem:
    def __init__(self):
        self.declarations = []

    def create_declaration(self, declaration_id, traveler_name, items, compliance_status):
        declaration = CustomsDeclaration(declaration_id, traveler_name, items, compliance_status)
        self.declarations.append(declaration)
        return declaration

    def read_declaration(self, declaration_id):
        for declaration in self.declarations:
            if declaration.declaration_id == declaration_id:
                return declaration
        return None

    def update_declaration(self, declaration_id, traveler_name=None, items=None, compliance_status=None):
        declaration = self.read_declaration(declaration_id)
        if declaration:
            if traveler_name:
                declaration.traveler_name = traveler_name
            if items:
                declaration.items = items
            if compliance_status is not None:
                declaration.compliance_status = compliance_status
            return declaration
        return None

    def delete_declaration(self, declaration_id):
        declaration = self.read_declaration(declaration_id)
        if declaration:
            self.declarations.remove(declaration)
            return declaration
        return None

    def process_customs_declarations(self, declaration_id):
        declaration = self.read_declaration(declaration_id)
        if declaration:
            declaration.compliance_status = "Processed"
            return declaration
        return None

    def track_declaration_compliance(self, declaration_id):
        declaration = self.read_declaration(declaration_id)
        if declaration:
            return declaration.compliance_status
        return "Declaration not found"


def main():
    system = CustomsDeclarationSystem()

    while True:
        print("\nCustoms Declaration System Menu:")
        print("1. Create Declaration")
        print("2. Read Declaration")
        print("3. Update Declaration")
        print("4. Process Declaration")
        print("5. Track Compliance")
        print("6. Delete Declaration")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ")

        if choice == '1':
            declaration_id = input("Enter Declaration ID: ")
            traveler_name = input("Enter Traveler Name: ")
            items = input("Enter Items (comma-separated): ").split(',')
            compliance_status = input("Enter Compliance Status: ")
            declaration = system.create_declaration(declaration_id, traveler_name.strip(), [item.strip() for item in items], compliance_status)
            print(f"\nCreated Declaration: {declaration.__dict__}")

        elif choice == '2':
            declaration_id = input("Enter Declaration ID to read: ")
            declaration = system.read_declaration(declaration_id)
            if declaration:
                print(f"\nRead Declaration: {declaration.__dict__}")
            else:
                print("Declaration not found.")

        elif choice == '3':
            declaration_id = input("Enter Declaration ID to update: ")
            traveler_name = input("Enter new Traveler Name (leave blank to keep current): ")
            items = input("Enter new Items (comma-separated, leave blank to keep current): ")
            compliance_status = input("Enter new Compliance Status (leave blank to keep current): ")

            items = [item.strip() for item in items.split(',')] if items else None
            declaration = system.update_declaration(declaration_id, traveler_name.strip() or None, items, compliance_status or None)
            if declaration:
                print(f"\nUpdated Declaration: {declaration.__dict__}")
            else:
                print("Declaration not found.")

        elif choice == '4':
            declaration_id = input("Enter Declaration ID to process: ")
            processed_declaration = system.process_customs_declarations(declaration_id)
            if processed_declaration:
                print(f"\nProcessed Declaration: {processed_declaration.__dict__}")
            else:
                print("Declaration not found.")

        elif choice == '5':
            declaration_id = input("Enter Declaration ID to track compliance: ")
            compliance_status = system.track_declaration_compliance(declaration_id)
            print(f"\nCompliance Status: {compliance_status}")

        elif choice == '6':
            declaration_id = input("Enter Declaration ID to delete: ")
            deleted_declaration = system.delete_declaration(declaration_id)
            if deleted_declaration:
                print(f"\nDeleted Declaration: {deleted_declaration.__dict__}")
            else:
                print("Declaration not found.")

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
