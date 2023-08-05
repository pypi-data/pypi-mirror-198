/* Copyright 2023 The StableHLO Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef STABLEHLO_DIALECT_VHLOTYPES_H
#define STABLEHLO_DIALECT_VHLOTYPES_H

#include "llvm/ADT/ArrayRef.h"
#include "llvm/ADT/SmallVector.h"
#include "mlir/IR/Attributes.h"
#include "mlir/IR/MLIRContext.h"
#include "mlir/IR/OpImplementation.h"
#include "mlir/Transforms/DialectConversion.h"
#include "stablehlo/dialect/Version.h"

namespace mlir {
namespace vhlo {

class VhloTypeConverterBase : public TypeConverter {
 public:
  VhloTypeConverterBase() : TypeConverter(){};

  virtual ~VhloTypeConverterBase() = default;

  virtual Attribute convertEncoding(Attribute attr) = 0;
};

// This class is used to manage conversions between VHLO and Builtin
// dialects.
class VhloTypeConverter : public VhloTypeConverterBase {
 public:
  VhloTypeConverter() : VhloTypeConverterBase() {}

  // A subclass can call this method to add conversions from VHLO -> Builtin
  // types. Note that conversions are applied in reverse order, with the most
  // recently added conversion attempted to be applied first. Because of this,
  // it is likely that a subclass should call this last, especially if a default
  // `Type -> Type` fallback conversion is registered.
  void addVhloToBuiltinConversions();

  // A subclass can call this method to add conversions from  Builtin -> VHLO
  // types. Note that conversions are applied in reverse order, with the most
  // recently added conversion attempted to be applied first. Because of this,
  // it is likely that a subclass should call this last, especially if a default
  // `Type -> Type` fallback conversion is registered.
  void addBuiltinToVhloConversions();
};

// Autogenerated VHLO type printers and parsers.
LogicalResult printVhloType(Type type, AsmPrinter& printer);
OptionalParseResult parseVhloType(mlir::AsmParser& parser,
                                  llvm::StringRef* mnemonic, mlir::Type& type);

// Registers VHLO types in a given context.
// See comments for `VhloDialect::addVhloTypes` for additional details.
void registerVhloTypes(MLIRContext* context);

}  // namespace vhlo
}  // namespace mlir

#include "stablehlo/dialect/VhloTypeInterfaces.h.inc"
#define GET_TYPEDEF_CLASSES
#include "stablehlo/dialect/VhloTypeDefs.h.inc"

#endif  // STABLEHLO_DIALECT_VHLOTYPES_H
